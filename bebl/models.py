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

    def _as_dict(self):
        return {
            "uuid": self.uuid,
            "title": self.title,
            "content": self.content,
            "author_uuid": self.author_uuid,
            "created_at": self.created_at.isoformat(),
        }


@dataclass
class Comment:
    uuid: UUID
    content: str
    author_id: UUID
    post_id: UUID
    created_at: datetime

    def _as_dict(self):
        return {
            "uuid": self.uuid,
            "content": self.content,
            "author_id": self.author_id,
            "post_id": self.post_id,
            "created_at": self.created_at.isoformat(),
        }
