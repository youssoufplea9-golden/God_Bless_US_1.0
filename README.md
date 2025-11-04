#  Smart File Organizer

A simple yet powerful **Python script** that automatically organizes files from a source folder into categorized subfolders (like *Images*, *Documents*, *Videos*, etc...).  
This is a simple way for cleaning up your **Downloads**, **Desktop**, or **project folders** **etc...**

---

##  Features

✅ Automatically detects file types and sorts them into predefined categories  
✅ Works on **Windows**, **macOS**, and **Linux**  
✅ Command-line interface using `argparse`  
✅ Safely skips folders and invalid files  
✅ Creates destination folders automatically  
✅ Fully customizable — add or modify file categories easily  

---

## Categories

The script organizes files into these main folders:

| Category | Extensions |
|-----------|-------------|
| **Images** | .jpg, .jpeg, .png, .gif, .bmp, .svg |
| **Documents** | .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .txt, .csv |
| **Music** | .mp3, .wav, .aac |
| **Videos** | .mp4, .mov, .avi, .mkv |
| **Archives** | .zip, .rar, .7z |
| **Programs** | .exe, .msi |
| **Other** | Any file that doesn’t match the above |

---

##  Installation

### 1. Clone or Download this Repository
```bash
git clone https://github.com/yourusername/file-organizer.git
cd file-organizer
```

### 2. Run with Python
Make sure you have Python 3.7+ installed:
```bash
python organizer.py
```

---

## Usage

You can run the script **interactively** or via **the command-line arguments**.

### Option 1: Interactive Mode
Just run:
```bash
python organizer.py
///
The program will ask you :
///
Source path (e.g., C:\Users\You\Downloads):
Destination path (press Enter to use 'Organized'):
///

### Option 2: Command-Line Arguments
```bash
python organizer.py -s "C:\Users\You\Downloads" -d "C:\Users\You\Organized"
```

**Arguments:**
| Flag | Description | Example |
|------|--------------|----------|
| `-s`, `--source` | Folder to scan and organize | `C:\Users\You\Downloads` |
| `-d`, `--dest` | Folder where organized files are stored | `C:\Users\You\Organized` |

---

## 🛠️ How Does it Works :

1. Scans all files in the source folder.  
2. Determines their category based on file extension.  
3. Creates subfolders in the destination folder (if they don’t exist).  
4. Moves files into their respective subfolders.  
5. Prints a summary of moved files.

Example output:
```
Scanning source folder: C:\Users\You\Downloads
Destination folder: C:\Users\You\Organized
Moved: photo1.jpg  ->  Images/
Moved: resume.pdf  ->  Documents/
Moved: song.mp3    ->  Music/
Organization complete.
3 file(s) moved.
```

---

## ✏️ Customization :

You can easily modify or extend the file type categories in the script:
///python
CATEGORIES = {
    ".jpg": "Images",
    ".pdf": "Documents",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".zip": "Archives",
    ".exe": "Programs",
}
///
Just edit or add new extensions and rerun the script!

----

##  Optional Enhancements :

- Add duplicate file handling (auto-rename files instead of overwriting)  
- Skip hidden/system files  
- Add MIME-type detection for smarter classification  
- Create a log file of all moved files  

----



## 👨‍💻 Authors :

**Youssouf Plea**  **HUMAM TAHSEEN ABULLAH AL-MOHAMMED** **Othman Murtala Abubakar**

Thanks
