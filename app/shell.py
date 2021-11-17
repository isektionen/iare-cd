import subprocess
from pathlib import PurePath
from os import getcwd


def create_shell():
    cwd = getcwd()

    path = PurePath(cwd)
    if path.name == "iare-cms":
        return lambda x: subprocess.Popen(
            x, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, shell=True
        )
    else:
        return lambda x: subprocess.Popen(
            f"cd iare-cms; {x}",
            stdin=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            shell=True,
        )
