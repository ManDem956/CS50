import os
import shutil


def sort_by_extension(u_dir):

    Document_Files = [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt"]
    Image_Files = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"]
    Audio_Files = [".mp3", ".wav", ".aac", ".flac", ".wma"]
    Video_files = [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv"]
    Compressed_Files = [".zip", ".rar", ".7z", ".tar", ".gz"]
    Programming_Files = [".py", ".js", ".html", ".css", ".java"]

    extension_dict = {
        "Document_Files": Document_Files,
        "Image_Files": Image_Files,
        "Audio_Files": Audio_Files,
        "Video_files": Video_files,
        "Compressed_Files": Compressed_Files,
        "Programming_Files": Programming_Files,
    }

    for dir_path, dir_name, file_name in os.walk(u_dir):
        for file in file_name:
            file_path = os.path.join(dir_path, file)
            file_extension = os.path.splitext(file)[1].lower()
            moved = False

            for extension_str, extension_type in extension_dict.items():
                if file_extension in extension_type:
                    category = os.path.join(u_dir, extension_str)
                    os.makedirs(category, exist_ok=True)
                    shutil.move(file_path, os.path.join(category, file))
                    moved = True
                    break

            if not moved:
                unknown_category = os.path.join(u_dir, "Unknown")
                os.makedirs(unknown_category, exist_ok=True)
                shutil.move(file_path, os.path.join(unknown_category, file))
