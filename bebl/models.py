from uuid import UUID
from datetime import datetime
from dataclasses import dataclass


@dataclass
class User:
    uuid: UUID
    username: str
    email: str
    password: str
    created_at: datetime


@dataclass
class Post:
    uuid: UUID
    title: str
    content: str
    author_uuid: UUID
    created_at: datetime


@dataclass
class Comment:
    uuid: UUID
    content: str
    author_id: UUID
    post_id: UUID
    created_at: datetime
