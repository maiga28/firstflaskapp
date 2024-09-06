from main_apps.accounts.accounts_models import accounts_user as user
from flask import Blueprint, render_template, request, redirect, url_for, flash
from main_apps.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.security import check_password_hash


accounts = Blueprint('accounts', __name__)

from werkzeug.security import generate_password_hash

@accounts.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        uname = request.form.get('uname')
        mail = request.form.get('mail')
        passw = request.form.get('passw')

        # Hachage du mot de passe avec la méthode recommandée
        hashed_password = generate_password_hash(passw, method='pbkdf2:sha256')

        # Création de l'utilisateur
        new_user = user(username=uname, email=mail, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('accounts.login'))
    
    return render_template("accounts/register.html")




@accounts.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Récupérer les données du formulaire
        mail = request.form.get('mail')
        passw = request.form.get('passw')

        # Vérifier si l'utilisateur existe
        existing_user = user.query.filter_by(email=mail).first()

        if existing_user and check_password_hash(existing_user.password, passw):
            # Connexion réussie
            flash("Login successful!", "success")
            return redirect(url_for("posts.all_posts"))
        else:
            # Erreur d'authentification
            flash("Invalid email or password", "error")
            return redirect(url_for('accounts.login'))

    return render_template("accounts/login.html")

