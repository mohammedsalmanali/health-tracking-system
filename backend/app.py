# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    from routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5005)
