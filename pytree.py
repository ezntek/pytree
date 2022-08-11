#!/usr/bin/env python3

from Xlib.error import ConnectionClosedError
import subprocess, os, sys, colorama
from pynput import keyboard

class Directory():
    def __init__(self, name: str, collapsed: bool) -> None:
        self.name = name
        self.is_collapsed = collapsed

    def __repr__(self) -> str:
        if self.is_collapsed:
            return f"{colorama.Fore.GREEN}\033[1m[D]→ {self.name}\033[0m"
        else:
            return f"{colorama.Fore.GREEN}\033[1m[D]↓ {self.name}\033[0m"

class File():
    def __init__(self, name: str, can_exec: bool) -> None:
        self.name = name
        self.is_executable = can_exec

    def __repr__(self) -> str:
        if self.is_executable:
            return f"{colorama.Fore.YELLOW}\033[1m[F]* {self.name}\033[0m"
        else:
            return f"[F]  {self.name}"

def format_entry_as_class(current_dir: str, file_name: str):
    if os.path.isfile(os.path.join(current_dir, file_name)):
        if os.access(os.path.join(current_dir, file_name), os.X_OK):
            return File(name=file_name, can_exec=True)
        else:
            return File(name=file_name, can_exec=False)
    elif os.path.isdir(os.path.join(current_dir, file_name)):
        return Directory(name=file_name, collapsed=True)


def load(current_dir: str):
    return [format_entry_as_class(current_dir,listing) for listing in os.listdir()]

def arrowify(text: str):
    return f"{colorama.Fore.BLUE}\033[1m> \033[0m{text}"

def main():
    current_dir: str = "./"
    try:
        current_dir = sys.argv[1]
    except IndexError:
        current_dir = "./"

    should_close = False
    dir_classes = []
    selection_ptr: int = 0
    needs_reload = False
    has_init_load = False

    def hotkey_r():
        nonlocal needs_reload
        needs_reload = True
    
    def hotkey_q():
        sys.exit(0)

    hotkeys = [
        keyboard.HotKey(
            [keyboard.KeyCode(char='r')],
            hotkey_r,
        ),
        keyboard.HotKey(
            [keyboard.KeyCode(char='q')],
            hotkey_q,
        ),
    ]

    def signal_press_to_hotkeys(key):
        for hotkey in hotkeys:
            hotkey.press(l.canonical(key))

    def signal_release_to_hotkeys(key):
        for hotkey in hotkeys:
            hotkey.release(l.canonical(key))

    while not should_close:
        subprocess.run("clear")
        if needs_reload or not has_init_load:
            needs_reload = False
            has_init_load = True
            dir_classes = load(current_dir)
        for count, listing in enumerate(dir_classes):
            if count == selection_ptr:
                print(f"{arrowify(listing)}")
            else:
                print(f"  {listing}") 
        try:
            with keyboard.Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys) as l:
                l.join()
        except ConnectionClosedError:
            exit(0)

if __name__ == "__main__": main()
