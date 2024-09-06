from main_apps.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)  # Nom d'utilisateur obligatoire
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email obligatoire
    password = db.Column(db.String(60), nullable=False)  # Mot de passe obligatoire
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')  # Facultatif avec une valeur par défaut
    posts = db.relationship('Post', backref='author', lazy=True)  # Relation avec les posts, facultatif

    def __init__(self, username, email, password, image_file=None):
        self.username = username
        self.email = email
        self.password = password
        if image_file:
            self.image_file = image_file
