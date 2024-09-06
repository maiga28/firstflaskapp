from main_apps.posts.post_models import Post
from flask import Blueprint, render_template, request, redirect, url_for
from main_apps.extensions import db

posts = Blueprint('posts', __name__)

# Route pour afficher tous les posts
@posts.route("/")
@posts.route("/posts")
def all_posts(): 
    posts_list = Post.query.all()
    return render_template('posts/posts.html', posts=posts_list)

# Route pour créer un nouveau post
@posts.route("/")
@posts.route("/create", methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = request.form['user_id']
        new_post = Post(title=title, content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts.all_posts'))

    return render_template('posts/create_post.html')

# Route pour afficher un post spécifique
@posts.route("/posts/<int:id>")
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template('posts/post_detail.html', post=post)

# Route pour mettre à jour un post existant
@posts.route("/posts/<int:id>/update", methods=['GET', 'POST'])
def update_post(id):
    post = Post.query.get_or_404(id)
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.user_id = request.form['user_id']
        db.session.commit()
        return redirect(url_for('posts.post_detail', id=post.id))
    
    return render_template('posts/update_post.html', post=post)

# Route pour supprimer un post
@posts.route("/posts/<int:id>/delete", methods=['POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.all_posts'))
