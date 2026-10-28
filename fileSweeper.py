import os
from pathlib import Path
import send2trash  ## for recycle bin

directory = input("Enter full path: ").strip()


def sweepFolder(folder):
    for folderName, subFolders, fileNames in os.walk(folder):
        folderName = Path(folderName)
        print(f"scraping folder {folderName}...")

        for fileName in fileNames:
            fileSize = os.path.getsize(folderName / fileName) / 1_000_000
            print(f"file {fileName}...", end="")
            print(f"{os.path.getsize(folderName / fileName) / 1_000_000:.2f}MB")

            if fileSize >= 20:
                # os.unlink(folderName / fileName)
                # send2trash.send2trash(folderName / fileName)
                print(f"{fileName} deletedd")
            else:
                continue
    print("donezosdkakjskldjas.")


sweepFolder(directory)
