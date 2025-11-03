import os
import shutil
import argparse
import sys

# 1. Define categories using a dictionary
# This is the "smart" way to map extensions to folders
CATEGORIES = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".txt": "Documents",
    ".csv": "Documents",

    # Audio
    ".mp3": "Music",
    ".wav": "Music",
    ".aac": "Music",

    # Video
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    # Programs
    ".exe": "Programs",
    ".msi": "Programs",
}

def organize_directory(source_dir, dest_dir):
    """
    Scans the source folder and moves files into the destination folder,
    creating subfolders for each category.
    """
    
    # F-string for clear user feedback
    print(f"Scanning source folder: {source_dir}")
    print(f"Destination folder: {dest_dir}")
    
    # 2. Go through all files in the source folder
    # Using os.listdir()
    try:
        filenames = os.listdir(source_dir)
    except FileNotFoundError:
        print(f"ERROR: Source folder '{source_dir}' does not exist.", file=sys.stderr)
        return
    except NotADirectoryError:
        print(f"ERROR: Source path '{source_dir}' is not a folder.", file=sys.stderr)
        return

    if not filenames:
        print("Source folder is empty. No action required.")
        return

    # Loop to process each file
    files_moved = 0
    for filename in filenames:
        source_path = os.path.join(source_dir, filename) # Using os.path.join()
        
        # Make sure it's a file, not a folder
        if not os.path.isfile(source_path):
            print(f"Skipped (it's a folder): {filename}")
            continue

        # 3. Get the file extension and make it lowercase
        # Using string methods
        # os.path.splitext is safer than .split()
        file_ext = os.path.splitext(filename)[1].lower()

        # 4. Find the category or use "Other"
        category = CATEGORIES.get(file_ext, "Other")
        
        # 5. Create the destination subfolder if it doesn't exist
        dest_folder_path = os.path.join(dest_dir, category)
        
        # os.makedirs(..., exist_ok=True) creates the folder
        # without an error if it already exists
        os.makedirs(dest_folder_path, exist_ok=True)
        
        # 6. Move the file
        dest_path = os.path.join(dest_folder_path, filename)
        
        try:
            # Using shutil.move()
            shutil.move(source_path, dest_path)
            print(f"Moved: {filename}  ->  {category}/")
            files_moved += 1
        except Exception as e:
            print(f"ERROR moving {filename}: {e}", file=sys.stderr)

    print("\nOrganization complete.")
    print(f"{files_moved} file(s) moved.")

def main():
    """
    Main function to handle command-line arguments.
    Uses argparse. If paths are not given, it will ask the user.
    """
    parser = argparse.ArgumentParser(description="Organizes files from a source folder into a destination folder by type.")
    
    # Optional arguments: if missing, user will be prompted
    parser.add_argument("-s", "--source", 
                        type=str, 
                        required=False, 
                        help="The source folder to scan (e.g., C:\\Users\\You\\Downloads)")
    
    parser.add_argument("-d", "--dest", 
                        type=str, 
                        required=False, 
                        help="The folder to store the organized files")
    
    args = parser.parse_args()
    
    source = args.source
    dest = args.dest

    # If not provided, ask the user
    if not source:
        source = input("Source path (e.g., C:\\Users\\You\\Downloads): ").strip()
        if not source:
            print("No source path provided.", file=sys.stderr)
            sys.exit(1)

    # By default, suggest an 'Organized' folder next to the source
    if not dest:
        default_dest = os.path.join(os.path.dirname(source) or os.getcwd(), "Organized")
        dest_prompt = input(f"Destination path (press Enter to use '{default_dest}'): ").strip()
        dest = dest_prompt or default_dest

    # Normalize paths and create the destination folder if needed
    source = os.path.abspath(os.path.expanduser(source))
    dest = os.path.abspath(os.path.expanduser(dest))
    os.makedirs(dest, exist_ok=True)

    # If you also want to create the source folder if it doesn't exist:
    if not os.path.exists(source):
        print(f"Source folder '{source}' does not exist. Creating it...")
        os.makedirs(source, exist_ok=True)

    # Call the main organizing function
    organize_directory(source, dest)

# Standard professional script structure
if __name__ == "__main__":
    main()