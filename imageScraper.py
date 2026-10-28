from pathlib import Path
import os
import shutil

directory = input("Enter full path: ").strip()
ho = Path(__file__).parent / "yo"
ho.mkdir(parents=True, exist_ok=True)

extensions = (
    ".png",
    ".jpg",
    ".jpeg",
    ".jfif",
    ".webp",
    ".gif",
    ".bmp",
    ".tif",
    ".tiff",
    ".svg",
    ".ico",
    ".avif",
    ".heif",
    ".heic",
    ".dng",
    ".cr2",
    ".nef",
    ".arw",
)


def moveImage(folder):

    for folderName, subFolders, fileNames in os.walk(folder):
        folderName = Path(folderName)
        print(f"scraping folder {folderName}...")

        for fileName in fileNames:
            yo = fileName.lower().endswith(extensions)
            # print(fileName)

            if yo == True:
                dest = ho / fileName
                counter: int = 1

                while dest.exists():
                    dest = Path(
                        ho / f"{Path(fileName).stem}_{counter}{Path(fileName).suffix}"
                    )
                    counter += 1
                shutil.copy(folderName / fileName, dest)
                print(f"Adding file {fileName}...")
            else:
                continue
    print("donezosdkakjskldjas.")


moveImage(directory)
