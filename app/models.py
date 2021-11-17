from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Author(BaseModel):
    email: str
    name: str
    username: str


class Committer(BaseModel):
    email: str
    name: str
    username: str


class Commit(BaseModel):
    added: List[str]
    author: Author
    committer: Committer
    distinct: bool
    id: str
    message: str
    modified: List[str]
    removed: List
    timestamp: str
    tree_id: str
    url: str


class Author1(BaseModel):
    email: str
    name: str
    username: str


class Committer1(BaseModel):
    email: str
    name: str
    username: str


class HeadCommit(BaseModel):
    added: List[str]
    author: Author1
    committer: Committer1
    distinct: bool
    id: str
    message: str
    modified: List[str]
    removed: List
    timestamp: str
    tree_id: str
    url: str


class Pusher(BaseModel):
    email: str
    name: str


class Owner(BaseModel):
    avatar_url: str
    email: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    name: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str


class Repository(BaseModel):
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int
    default_branch: str
    deployments_url: str
    description: Any
    disabled: bool
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: Any
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: str
    languages_url: str
    license: Any
    master_branch: str
    merges_url: str
    milestones_url: str
    mirror_url: Any
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    owner: Owner
    private: bool
    pulls_url: str
    pushed_at: int
    releases_url: str
    size: int
    ssh_url: str
    stargazers: int
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    updated_at: str
    url: str
    watchers: int
    watchers_count: int


class Sender(BaseModel):
    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str


class GithubModel(BaseModel):
    after: str
    base_ref: Any
    before: str
    commits: List[Commit]
    compare: str
    created: bool
    deleted: bool
    forced: bool
    head_commit: HeadCommit
    pusher: Pusher
    ref: str
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
