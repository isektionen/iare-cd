from util import find


SERVICES = [
    {
        "name": "iare-cms",
        "repo": "https://github.com/isektionen/iare-cms",
        "to-path": "/iare-cms",
        "build-command": "git restore .;git pull;yarn;yarn build;pm2 restart iare-cms;",
    },
]


def get_service(name: str):
    return find(lambda p: p["name"] == name, SERVICES)