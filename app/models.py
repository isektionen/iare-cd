from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Config(BaseModel):
    content_type: str
    insecure_ssl: str
    url: str


class LastResponse(BaseModel):
    code: Any
    status: str
    message: Any


class Hook(BaseModel):
    type: str
    id: int
    name: str
    active: bool
    events: List[str]
    config: Config
    updated_at: str
    created_at: str
    url: str
    test_url: str
    ping_url: str
    deliveries_url: str
    last_response: LastResponse


class Owner(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


class License(BaseModel):
    key: str
    name: str
    spdx_id: str
    url: str
    node_id: str


class Repository(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: Owner
    html_url: str
    description: str
    fork: bool
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: str
    size: int
    stargazers_count: int
    watchers_count: int
    language: str
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    forks_count: int
    mirror_url: Any
    archived: bool
    disabled: bool
    open_issues_count: int
    license: License
    allow_forking: bool
    is_template: bool
    topics: List[str]
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str


class Sender(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


class GithubModel(BaseModel):
    zen: str
    hook_id: int
    hook: Hook
    repository: Repository
    sender: Sender


class SshKeyFingerprints(BaseModel):
    SHA256_RSA: str
    SHA256_DSA: str
    SHA256_ECDSA: str
    SHA256_ED25519: str


class GithubMetaModel(BaseModel):
    verifiable_password_authentication: bool
    ssh_key_fingerprints: SshKeyFingerprints
    hooks: List[str]
    web: List[str]
    api: List[str]
    git: List[str]
    packages: List[str]
    pages: List[str]
    importer: List[str]
    actions: List[str]
    dependabot: List[str]
