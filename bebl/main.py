from flask import Flask
from bebl.routes.posts import bp_posts
from bebl.routes.comments import bp_comments


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_posts)
    app.register_blueprint(bp_comments)
    return app
