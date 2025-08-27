import os
import shutil


path=input(r"Enter location of folder : ")
os.chdir(path)
contents=os.listdir()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx",".csv"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Code": [".py", ".cpp", ".java", ".js"],
    "Others": []
}

for ft in file_types.keys():
    os.makedirs(os.path.join(path,ft),exist_ok=True)
for item in contents:
    file_name,file_ext=os.path.splitext(item)
    for typ,ext in file_types.items():
        if file_ext in ext:
            shutil.move(os.path.join(path,item),os.path.join(path,typ,item))
            break
print("Your files are organized")


