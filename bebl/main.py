from typing import Any, Dict, Optional, Union

from flask import Flask

from bebl import exts
from bebl.config import Config
from bebl.routes.comments import bp_comments
from bebl.routes.posts import bp_posts


def create_app():
    settings = Config()
    app = Flask(__name__)
    app.config.from_object(settings)
    exts.db.init_app(app)
    exts.bcrypt.init_app(app)
    exts.migrate.init_app(app, exts.db)
    app.register_blueprint(bp_posts)
    app.register_blueprint(bp_comments)
    return app
