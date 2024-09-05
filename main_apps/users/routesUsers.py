from flask import Blueprint, render_template, request, redirect, url_for
from main_apps.users.user_models import User
from main_apps.extensions import db
from flask_wtf import FlaskForm
from wtforms import HiddenField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

users = Blueprint('users', __name__)

@users.route("/")
def all_users():
    users_list = User.query.all()
    limited_users = users_list[:10] 
    return render_template('users/users.html',users=limited_users)

@users.route("/create", methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Créez un utilisateur sans `image_file` et `posts`
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('users.all_users'))

    return render_template('users/create_user.html')

@users.route("/users/<int:id>/update", methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.password = request.form['password']  # Assurez-vous de hacher le mot de passe avant de le stocker
        db.session.commit()
        return redirect(url_for('users.all_users'))

    return render_template('users/update_user.html', user=user)


class DeleteForm(FlaskForm):
    hidden_tag = HiddenField()  # Exemple de champ caché

@users.route("/users/<int:id>/delete", methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.all_users'))

@users.route("/users/<int:id>/confirm_delete")
def confirm_delete(id):
    form = DeleteForm()
    return render_template('confirm_delete.html', form=form, user_id=id)
