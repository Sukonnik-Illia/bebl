from datetime import datetime
from uuid import uuid4
from flask import Flask, jsonify, request
from bebl.models import Post, User, Comment

app = Flask(__name__)


class Db:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_posts(self):
        return self.posts


db = Db()


@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(
        [
            {
                "title": post.title,
                "uuid": post.uuid,
            }
            for post in db.get_posts()
        ]
    )


@app.route("/posts", methods=["POST"])
def create_post():
    post = Post(uuid=uuid4(), **request.json, created_at=datetime.now())
    db.add_post(post)
    return jsonify(post)
