import uuid

from bebl.exts import bcrypt, db

# TODO: we should not create app here


class User(db.Model):
    uuid = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    posts = db.relationship("Post", backref="author")
    comments = db.relationship("Comment", backref="author")

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Post(db.Model):
    uuid = db.Column(db.String(36), primary_key=True, default=uuid.uuid4())
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_uuid = db.Column(db.String(36), db.ForeignKey("User.uuid"), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    author = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", backref="post")


class Comment(db.Model):
    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content = db.Column(db.Text, nullable=False)
    author_uuid = db.Column(db.String(36), db.ForeignKey("User.uuid"), nullable=False)
    post_uuid = db.Column(db.String(36), db.ForeignKey("Post.uuid"), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    post = db.relationship("Post", back_populates="comments")
    author = db.relationship("User", back_populates="comments")
