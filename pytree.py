#!/usr/bin/env python3

import subprocess, os, sys, colorama
from pynput import Key, HotKey, KeyCode, Listener

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
        if is_executable:
            return f"{colorama.Fore.YELLOW}\033[1m[F]* {self.name}\033[0m"
        else:
            return f"{colorama.Fore.YELLOW}\033[1m[F]  {self.name}\033[0m"

def format_entry_as_class(current_dir: str, file_name: str):
    if os.isfile(os.path.join(current_dir, file_name)):
        if os.access(os.path.join(current_dir, file_name), os.X_OK):
            return File(name=file_name, can_exec=True)
        else:
            return FIle(name=file_name, can_exec=False)


def load():
    return []

def main():
    should_close = False
    dir_classes = []
    selection_ptr: int = 0

    while not should_close:
        pass
    
if __name__ == "__main__":
    main()
