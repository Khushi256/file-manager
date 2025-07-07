# 📂 Smart File Organizer and Cleaner using Python

This is a lightweight Python automation script that helps you keep your folders clean and organized by:

✅ Organizing files into folders based on their **creation date**  
🧹 Deleting **temporary files** that haven’t been used in a while (default: 30 days)

---

## 🚀 Features

- Automatically moves files into date-based folders like `2025-06-29`
- Deletes old files containing "temp" in their names if:
  - They haven’t been accessed or modified in the last 30 days (customizable)
- Simple to run and easy to modify
- Uses built-in Python modules only — no external libraries needed

---

## 🛠️ How It Works

### 1. **Organize Files by Date**
Files in the target folder are scanned and moved into folders named after their creation date.

```python
C:\...\trial\example.pdf  →  C:\...\trial\2025-06-29\example.pdf
```
### 2. **Delete Old Temporary Files**

The script includes a function that **automatically deletes temporary files** — files with `"temp"` in their name — if they haven’t been accessed or modified for a certain number of days (default: `30` days).

### 🔍 How It Works

1. Recursively walks through the target folder and all its subdirectories.
2. Checks for files with `"temp"` (case-insensitive) in their name.
3. Compares the **last accessed** and **last modified** timestamps.
4. If both timestamps are older than the configured time limit (`DAYS_LIMIT`), the file is deleted.

### 🧠 Logic Behind the Check

```python
if (now - last_access > DAYS_LIMIT * 86400) and (now - last_modified > DAYS_LIMIT * 86400):
    os.remove(path)
```
## ⚙️ Configuration
Open the script and set the following variables at the top:

```python
TARGET_DIR = "C:\\Users\\YourUsername\\Path\\To\\Folder"
DAYS_LIMIT = 30  # Number of days before temp files are deleted
```
## ▶️ How to Run the Script

Follow these steps to run the Smart File Organizer and Cleaner on your machine:

### ✅ Step 1: Clone or Download the Repository

You can either clone the repository using Git or download the `.zip` file.

```bash
git clone https://github.com/Khushi256/file-manager.git
cd file-manager
```
### ✅ Step 2: Set the Configuration

Open the script and set the following variables at the top:

```bash
TARGET_DIR = "C:\\Users\\YourName\\Path\\To\\Folder"
DAYS_LIMIT = 30  # Set how old a temp file must be (in days) to delete it
```
Make sure the path you set in TARGET_DIR is correct and accessible.

### ✅ Step 3: Run the Script

Run the script from your terminal or IDE:

```bash
python file_organizer.py
```
## 🔮 Future Improvements

1. GUI using Tkinter or PyQt
2. File type-based filters (e.g., delete .log, .tmp)
3. Undo delete support (Recycle Bin)
4. Add scheduling with cron (Linux) or Task Scheduler (Windows)
5. Generate and store logs for moved/deleted files

## License
This project is open source and available under the MIT License.

