from flask import Blueprint, render_template
from main_apps.posts.post_models import Post

posts = Blueprint('posts', __name__)

@posts.route("/")
@posts.route("/posts")
def all_posts():
    posts = Post.query.all()
    return render_template('post/list_post.html', posts=posts)
