from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Owner(BaseModel):
    name: str
    email: Any
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
    owner: Optional[Owner] = None
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
    created_at: int
    updated_at: str
    pushed_at: int
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
    stargazers: int
    master_branch: str
    organization: str


class Pusher(BaseModel):
    name: str
    email: str


class Organization(BaseModel):
    login: str
    id: int
    node_id: str
    url: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: str


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


class Author(BaseModel):
    name: str
    email: str
    username: str


class Committer(BaseModel):
    name: str
    email: str
    username: str


class Commit(BaseModel):
    id: str
    tree_id: str
    distinct: bool
    message: str
    timestamp: str
    url: str
    author: Author
    committer: Committer
    added: List[str]
    removed: List
    modified: List


class Author1(BaseModel):
    name: str
    email: str
    username: str


class Committer1(BaseModel):
    name: str
    email: str
    username: str


class HeadCommit(BaseModel):
    id: str
    tree_id: str
    distinct: bool
    message: str
    timestamp: str
    url: str
    author: Author1
    committer: Committer1
    added: List[str]
    removed: List
    modified: List


class GithubModel(BaseModel):
    ref: Optional[str] = None
    before: Optional[str] = None
    after: Optional[str] = None
    repository: Optional[Repository] = None
    pusher: Optional[Pusher] = None
    organization: Optional[Organization] = None
    sender: Optional[Sender] = None
    created: Optional[bool] = None
    deleted: Optional[bool] = None
    forced: Optional[bool] = None
    base_ref: Optional[Any] = None
    compare: Optional[str] = None
    commits: Optional[List[Commit]] = None
    head_commit: Optional[HeadCommit] = None


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
