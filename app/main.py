from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends

from app.core.config import settings

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


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()


@app.get("/ping")
async def online():
    return {"status": "online"}


@app.post("/webhook/{service}", dependencies=[Depends(is_from_github)])
async def process(data: GithubModel, service: str):
    service = get_service(service)
    if is_main(data) and service:
        execute = create_shell(service)
        print("initiating CD..")
        execute(service["build-command"])
