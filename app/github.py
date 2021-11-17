from typing import List
from fastapi import Request
from httpx import AsyncClient
from ipaddress import ip_address, ip_network
from pprint import pprint

if __name__ == "__main__":
    from util import find, some
    from models import GithubModel, GithubMetaModel
    from services import SERVICES
else:
    from .util import find, some
    from .models import GithubModel, GithubMetaModel
    from .services import SERVICES

from git.repo import Repo

ALLOW_ALL = False


def is_main(payload: GithubModel):
    pushed_branch = payload.ref.replace("refs/heads/", "")
    main_branch = payload.repository.master_branch
    return pushed_branch == main_branch


async def get_meta() -> GithubMetaModel:
    async with AsyncClient() as client:
        meta = await client.get("https://api.github.com/meta")
        return meta.json()


def get_hook_whitelist(meta: GithubMetaModel):
    whitelist: List[str] = meta["hooks"]
    return whitelist


def ip_is_hook(src_ip: str, whitelist: List[str]):
    return some(lambda p: src_ip in ip_network(p), whitelist)


def clone(service: str):
    _service = find(lambda p: p["name"] == service, SERVICES)

    if _service:
        repo = _service["repo"]
        to_path = _service["to-path"]
        Repo.clone_from(repo, to_path)


async def is_from_github(request: Request):
    if ALLOW_ALL:
        return
    src_ip = ip_address(request.client.host)
    meta = await get_meta()
    whitelist = get_hook_whitelist(meta)
    pprint(src_ip)
    pprint(whitelist)
    if not ip_is_hook(src_ip, whitelist):
        raise Exception
