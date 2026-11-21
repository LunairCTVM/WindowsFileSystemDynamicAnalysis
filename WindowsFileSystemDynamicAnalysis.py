import os 
import sys
from pathlib import Path
import datetime
def clear():
    os.system('cls')

def main():
    clear()
    print("=== Windows File System Dynamic Analysis ===")
    path = input("Enter the path to analyze: ")
    clear()
    print(fr"[=] Analyse dynamique activee sur : {path}")

    folder = Path(path)
    known_items = {item.resolve() for item in folder.rglob("*")}
    while True:
            current_items = {item.resolve() for item in folder.rglob("*")}
            for item in folder.rglob("*"):
                if item.resolve() not in known_items:
                    known_items.add(item.resolve())

                    if item.is_file():
                        print(f"[+] New File: {item.name}")
                    elif item.is_dir():
                            print(f"[+] New Folder: {item.name}")

            for item_path in (known_items - current_items):
              print(f"[-] Deleted: {item_path.name}")
              known_items.remove(item_path)



if __name__ == "__main__":
    main()

