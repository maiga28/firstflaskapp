from flask import Blueprint, render_template
from main_apps.users.user_models import User

users = Blueprint('users', __name__)

@users.route("/")
@users.route("/users")
def all_users():
    users_list = User.query.all()
    return render_template('users/users.html', users=users_list)
