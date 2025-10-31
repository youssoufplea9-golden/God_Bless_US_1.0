import os
import shutil
from pathlib import Path

# --- Configuration ---
# Dictionary to map extensions to folder names.
# You can add, modify, or delete extensions/folders here.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".html", ".css", ".js", ".java", ".c", ".cpp"],
}

# Default folder name for uncategorized files
OTHER_FOLDER = "Others"

def organize_directory():
    """
    Scans the current directory, creates folders, and moves files 
    based on their extension.
    """
    # 1. Define the target directory (where the script is executed)
    current_dir = Path.cwd()
    print(f"Starting organization in: {current_dir}")

    # 2. Iterate through all items (files and folders)
    for item in current_dir.iterdir():
        # Ignore folders and the script itself
        if item.is_file() and item.name != Path(__file__).name:
            
            file_extension = item.suffix.lower()
            destination_folder_name = OTHER_FOLDER # Default: "Others"

            # 3. Determine the destination folder
            found_category = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    destination_folder_name = category
                    found_category = True
                    break
            
            # Define the full path of the destination folder
            destination_dir = current_dir / destination_folder_name
            
            # 4. Create the folder if it does not exist
            # exist_ok=True prevents an error if the folder already exists
            destination_dir.mkdir(exist_ok=True)
            
            # 5. Move the file
            try:
                shutil.move(str(item), str(destination_dir / item.name))
                print(f"Moved: '{item.name}' to '{destination_folder_name}/'")
            except shutil.Error as e:
                # Handle cases where the file already exists at the destination
                print(f"Move error for '{item.name}': File already exists or another error ({e})")

    print("\n✅ File sorting operation complete!")

if __name__ == "__main__":
    organize_directory()