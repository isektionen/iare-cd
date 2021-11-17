if __name__ == "__main__":
    from util import find
else:
    from .util import find


SERVICES = [
    {
        "name": "iare-cms",
        "repo": "https://github.com/isektionen/iare-cms",
        "to-path": "/iare-cms",
        "cwd": "/usr/ubuntu/iare-cms",
        "build-command": "git restore .;git pull;yarn;yarn build;pm2 restart iare-cms;",
    },
]


def get_service(name: str):
    return find(lambda p: p["name"] == name, SERVICES)