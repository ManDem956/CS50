import os
import shutil
from collections import ChainMap


def gen_extensions_dict():
    extensions_dict = {
        "Document_Files": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt"],
        "Image_Files": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"],
        "Audio_Files": [".mp3", ".wav", ".aac", ".flac", ".wma"],
        "Video_files": [".mp4", ".avi", ".mov", ".wmv", ".flv"],
        "Compressed_Files": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Programming_Files": [".py", ".js", ".html", ".css", ".java"],
    }

    """
    extensions_maps is a temporary generator of dictionaries in form:
            [
            {'.doc': 'Document_Files',
                '.docx': 'Document_Files',
                '.pdf': 'Document_Files',
                '.txt': 'Document_Files',
                '.rtf': 'Document_Files',
                '.odt': 'Document_Files'
            },
            {'.jpg': 'Image_Files',
                '.jpeg': 'Image_Files',
                '.png': 'Image_Files',
                '.gif': 'Image_Files',
                '.bmp': 'Image_Files',
                '.tif': 'Image_Files',
                '.tiff': 'Image_Files'
            },
            ...
            ]
    """
    extensions_maps = (dict(zip(values, [key]*len(values))) for key, values in extensions_dict.items())

    """
    combine a collection of dictionaries into one big dictionary
    result = {'.py': 'Programming_Files',
                '.js': 'Programming_Files',
                '.html': 'Programming_Files',
                '.css': 'Programming_Files',
                '.java': 'Programming_Files',
                '.zip': 'Compressed_Files',
                '.rar': 'Compressed_Files',
                '.7z': 'Compressed_Files',
                '.tar': 'Compressed_Files',
                '.gz': 'Compressed_Files',
                '.mp4': 'Video_files',
                '.avi': 'Video_files',
                '.mov': 'Video_files',
                '.wmv': 'Video_files',
                '.flv': 'Video_files',
                ...}
    """
    result = dict(ChainMap(*extensions_maps))
    return result


def main():
    users_dir = input("Your directory: ").strip()
    sort_by_extension(users_dir, gen_extensions_dict())


def sort_by_extension(u_dir: str, extensions_map: dict):
    for dir_path, _, files in os.walk(u_dir):
        for file in files:
            file_path = os.path.join(dir_path, file)
            file_extension = os.path.splitext(file)[1].lower()

            if extention_str := extensions_map.get(file_extension):
                cathegory = os.path.join(u_dir, extention_str)

                if not os.path.exists(cathegory):
                    os.makedirs(cathegory)

                shutil.move(file_path, os.path.join(cathegory, file))


if __name__ == "__main__":
    exit(main())
