import os,sys,shutil

def printLine():
    print("----------------------------------------")

def changeCWD(msg = 'Please enter absolute path\n'):
    newCWD = input(msg)
    try:
        printLine()
        print("Changing Working Directory -", newCWD)
        printLine()
        os.chdir(newCWD)
    except:
        changeCWD('Ooops! Invalid path entered\n\nPlease enter correct path\n')

cwd = os.getcwd()
print('Your current working directory is ', cwd)
printLine()

wantChangeCWD = input("Do you want to change the directory? y/n\n").lower()
answer = ['y', 'n']

while wantChangeCWD not in answer:
    printLine()
    print('--- Ooops! you entered wrong keyword ---')
    printLine()
    wantChangeCWD = input("Do you want to change the directory? y/n\n").lower()

if wantChangeCWD == 'y':
    changeCWD()

files = os.listdir()
if 'main.py' in files:
    files.remove('main.py')

fileExts = []
folders = ["images", "compressed", "documents", "executables", "medias", "progs", "others"]
imageExts = [".png", ".jpg", ".jpeg", "gif"]
compressedExts = [".gz", ".zip", ".gz", ".tar"]
documentExts = [".pdf", ".docx", ".csv", ".xlsx", ".xls", ".txt", ".doc"]
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
def clearTheClutter():
    numOfFilesProcessed = 0
    for file in files:
        filename, file_extension = os.path.splitext(file)
        folderName = getFolderNameByExt(file_extension)
        if os.path.isfile(file):
            print(f"{file} to {folderName}/{file}")
            os.replace(file, f"{folderName}/{file}")
            numOfFilesProcessed += 1 
    print("Total files processed:", numOfFilesProcessed)
    printLine()

for folder in folders:
    folder = folder.capitalize()
    printLine()
    print('Creating folder', folder)
    createDirIfNotExists(folder)

printLine()
print("Cleaning Now!!!")
printLine()

clearTheClutter()

print("Cleaning DONE!!!")
printLine()

print('Now removing unused folders')
allFolders = os.listdir()
for folder in allFolders:
    if folder[0] == '.': #Check wheather is this a executable or var folder
        continue
    if os.path.isdir(folder):
        if len(os.listdir(folder)) == 0 and folder.lower() in folders:
            shutil.rmtree(folder)
printLine()
print('Successfully DONE!!!')
printLine()
