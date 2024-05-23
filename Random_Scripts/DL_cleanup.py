import os
import shutil

def clean_downloads_folder(downloads_path):
    # Define directories to organize files
    directories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Music": [".mp3", ".wav", ".flac", ".ogg"],
        "Compressed": [".zip", ".rar", ".7z", ".tar.gz"],
        "Executables": [".exe", ".msi", ".dmg", ".apk"],
        "Others": []  # Default for files with unknown extensions
    }

    # Create directories if they don't exist
    for directory in directories:
        directory_path = os.path.join(downloads_path, directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    # Move files into appropriate directories
    for filename in os.listdir(downloads_path):
        if filename != "clean_downloads.py":  # Skip this script file
            file_path = os.path.join(downloads_path, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()
                moved = False
                for directory, extensions in directories.items():
                    if file_extension in extensions:
                        destination_dir = os.path.join(downloads_path, directory)
                        shutil.move(file_path, destination_dir)
                        moved = True
                        break
                if not moved:
                    destination_dir = os.path.join(downloads_path, "Others")
                    shutil.move(file_path, destination_dir)

    print("Downloads folder cleaned up successfully!")

if __name__ == "__main__":
    downloads_folder_path = "/home/eagleeyez/Downloads"  # Change this to your Downloads folder path
    clean_downloads_folder(downloads_folder_path)
