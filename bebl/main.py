from flask import Flask
from bebl.routes.posts import bp_posts


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_posts)
    return app
