import os
import shutil

Document_Files = [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt"]
Image_Files=[".jpg",".jpeg",".png",".gif",".bmp",".tif",".tiff"]
Audio_Files=[".mp3",".wav",".aac",".flac",".wma"]
Video_files=[".mp4",".avi",".mov",".wmv",".flv"]
Compressed_Files=[".zip",".rar",".7z",".tar",".gz"]
Programming_Files=[".py",".js",".html",".css",".java"]

extention_dict={
    "Document_Files":Document_Files,
    "Image_Files":Image_Files,
    "Audio_Files":Audio_Files,
    "Video_files":Video_files,
    "Compressed_Files":Compressed_Files,
    "Programming_Files":Programming_Files,
}

optimized_extentions_dict = {}
for category, extensions in extention_dict.items():
    for extension in extensions:
        optimized_extentions_dict[extension] = category


def main():
    users_dir=input("Your directory: ").strip()
    sort_by_extension(users_dir, optimized_extentions_dict)


def sort_by_extension(u_dir: str, extensions_map: dict):
    for dir_path, _, files in os.walk(u_dir):
        for file in files:
            file_path=os.path.join(dir_path,file)
            file_extension=os.path.splitext(file)[1].lower()

            if extention_str := extensions_map.get(file_extension):
                cathegory=os.path.join(u_dir,extention_str)
                
                if not os.path.exists(cathegory):
                    os.makedirs(cathegory)

                shutil.move(file_path,os.path.join(cathegory,file))


if __name__ == "__main__":
    exit(main())            