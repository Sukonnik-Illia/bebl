from datetime import datetime
from uuid import uuid4

from flask import Blueprint, jsonify, request

from bebl.db import db
from bebl.models import Post

bp_posts = Blueprint("posts", __name__, url_prefix="/posts")


@bp_posts.route("", methods=["GET"])
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


@bp_posts.route("", methods=["POST"])
def create_post():
    post = Post(uuid=uuid4(), **request.json, created_at=datetime.now(), author_uuid=uuid4())
    db.add_post(post)
    return jsonify(post._as_dict()), 201


@bp_posts.route("/<uuid:post_id>", methods=["GET"])
def get_post(post_id):
    post = db.get_post(post_id)
    if post is None:
        return "", 404
    return jsonify(post._as_dict())
