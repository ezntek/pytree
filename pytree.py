#!./env/bin/python
import os

def format_entry(file_or_dir: str) -> str:
    return "L " + file_or_dir

def load_folder(path: str) -> list[str]:
    return os.listdir(path)

def main() -> int:
    currentDir = "./"
    for listing in load_folder(currentDir):
        print(format_entry(listing))
    return 0

if __name__ == "__main__":
    exit(main())
