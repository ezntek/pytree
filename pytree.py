#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys, os

hidden_files = False

def parse(cmd: str, current_dir:str):
    if cmd == "h":
        hidden_files = True
    if cmd == "q":
        exit(0)
    
def load_dir(current_dir: str) -> str:
    retval = ""
    for listing in load_folder(current_dir):
        if os.path.isdir(os.path.join(current_dir, listing)):
            retval += format_entry_dir("collapsed",listing) + "\n"
        elif os.path.isfile(os.path.join(current_dir, listing)):
            retval += format_entry_file(listing) + "\n"

    return retval

def display_dir(current_dir: str):
    print(load_dir(current_dir))

def format_entry_dir(mode: str, dirname: str) -> str:
    if mode == "collapsed":
        return "→ " + dirname
    elif mode == "":
        return "↓ " + dirname

def format_entry_file(filename: str) -> str:
    return "- " + filename

def load_folder(path: str) -> list[str]:
    return os.listdir(path)

def get_header() -> str:
    return "PyTree ([h] for hidden files, [q] for quit)\n"

def main() -> int:

    while True:
        try:
            if os.path.exists(os.path.dirname(sys.argv[1])):
                current_dir = sys.argv[1]
            else:
                print("not a valid directory! please enter a valid path. defaulting to current path.")
                raise IndexError
        except IndexError:
            current_dir = "./"

        print(get_header())
        display_dir(current_dir)
        parse(input("command: "), current_dir)
        os.system("clear")
if __name__ == "__main__":
    exit(main())
