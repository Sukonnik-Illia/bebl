from uuid import UUID
from collections import defaultdict
from bebl.models import Post, Comment, User


class Db:
    def __init__(self):
        self.posts = {}
        self.users = {}
        self.comments = defaultdict(list)

    def clear_db(self):
        self.posts = {}
        self.users = {}
        self.comments = defaultdict(list)

    def add_post(self, post: Post):
        self.posts[post.uuid] = post

    def get_posts(self) -> list[Post]:
        return list(self.posts.values())

    def get_post(self, post_id: UUID) -> Post:
        return self.posts.get(post_id)

    def add_comment(self, comment: Comment):
        self.comments[comment.post_id].append(comment)

    def get_comments(self, post_id: UUID) -> list[Comment]:
        return list(self.comments[post_id])

    def add_user(self, user: User):
        self.users[user.uuid] = user

    def get_user(self, user_id: UUID) -> User:
        return self.users.get(user_id)


db = Db()
