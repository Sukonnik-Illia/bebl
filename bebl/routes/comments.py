from datetime import datetime
from uuid import uuid4

from flask import Blueprint, jsonify, request

from bebl.db import db
from bebl.models import Comment

bp_comments = Blueprint("comments", __name__, url_prefix="/posts/<uuid:post_id>/comments")


@bp_comments.route("", methods=["POST"])
def create_comment(post_id):
    comment = Comment(
        uuid=uuid4(),
        post_id=post_id,
        **request.json,
        created_at=datetime.now(),
        author_id=uuid4(),
    )
    db.add_comment(comment)
    return jsonify(comment._as_dict()), 201


@bp_comments.route("", methods=["GET"])
def get_comments(post_id):
    return jsonify([comment._as_dict() for comment in db.get_comments(post_id)])
