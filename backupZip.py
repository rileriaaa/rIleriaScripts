import zipfile, os
from pathlib import Path

directory = input("Enter full path: ").strip()


def backup(folder):
    folder = Path(folder)

    number = 1
    while True:
        zipName = Path(folder.parts[-1] + "-" + str(number) + ".zip")
        if not zipName.exists():
            break
        number += 1

    print(f"Creating {zipName}")
    backupZip = zipfile.ZipFile(zipName, "w")

    for folderName, subFolders, fileNames in os.walk(folder):
        folderName = Path(folderName)
        print(f"Adding files in folder {folderName}...")

        for fileName in fileNames:
            print(f"Adding file {fileName}...")
            backupZip.write(folderName / fileName)

    backupZip.close()
    print("Done.")


backup(directory)
