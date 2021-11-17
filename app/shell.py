import subprocess
from pathlib import PurePath
from os import getcwd


def create_shell(service):
    cwd = getcwd()

    path = PurePath(cwd)
    service_path = PurePath(service["cwd"])
    if path.name == service_path.name:
        return lambda x: subprocess.Popen(x, shell=True)
    else:
        return lambda x: subprocess.Popen(
            f"cd; cd {service['cwd']}; {x}",
            shell=True,
        )
