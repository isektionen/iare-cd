from fastapi import FastAPI
from fastapi.params import Depends

if __name__ == "__main__":
    from github import is_from_github, is_main
    from services import get_service
    from shell import create_shell
    from models import GithubModel
else:
    from .github import is_from_github, is_main
    from .services import get_service
    from .shell import create_shell
    from .models import GithubModel


def create_app():
    app = FastAPI()
    return app


app = create_app()


@app.post("/webhook/{service}", dependencies=[Depends(is_from_github)])
async def process(data: GithubModel, service: str):
    service = get_service(service)
    if is_main(data) and service:
        execute = create_shell()

        execute(service["build-command"])
