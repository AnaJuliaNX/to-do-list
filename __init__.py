from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod.db'
    app.config['SQLALCHEMY_TRACK_MIDIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.controllers.user_controller import user_bp
    from app.controllers.task_controller import task_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(task_bp)

    @app.router('/')
    def home():
        return render_template('index.html')

