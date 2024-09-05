from flask import Flask, render_template
from main_apps.extensions import db
from main_apps.posts.routesPost import posts as posts_router
from main_apps.users.routesUsers import users as users_router
from flask_migrate import Migrate

app = Flask(__name__)

# Configuration de la base de données

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation des extensions
db.init_app(app)
migrate = Migrate(app, db)


# Enregistrement des blueprints
app.register_blueprint(posts_router, url_prefix='/posts')
app.register_blueprint(users_router, url_prefix='/users')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
