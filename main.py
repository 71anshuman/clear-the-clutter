import os

files = os.listdir()
files.remove('main.py')

fileExts = []
folders = ["images", "compressed", "documents", "executables", "medias", "progs", "others"]
imageExts = [".png", ".jpg", ".jpeg", "gif"]
compressedExts = [".gz", ".zip", ".gz", ".tar"]
documentExts = [".pdf", ".docx", ".csv", ".xlsx", ".xls"]
executableExts = [".dmg", ".exe", ".msi", ".apk", ".pkg"]
mediaExts = [".mp4", "mp3", ".mov", ".mpeg"]
progExts = [".php", ".html", ".js", ".py", ".go", "java"]

def getFolderNameByExt(ext):
    if ext in imageExts:
        return folders[0]
    elif ext in compressedExts:
        return folders[1]
    elif ext in documentExts:
        return folders[2]
    elif ext in executableExts:
        return folders[3]
    elif ext in mediaExts:
        return folders[4]
    elif ext in progExts:
        return folders[5]
    else:
        return folders[6]

def createDirIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

for folder in folders:
    folder = folder.capitalize()
    createDirIfNotExists(folder)

for file in files:
    filename, file_extension = os.path.splitext(file)
    folderName = getFolderNameByExt(file_extension)
    if os.path.isfile(file):
        os.replace(file, f"{folderName}/{file}")
