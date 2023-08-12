# backend/app.py
from flask import Flask                          # pylint: disable=import-error
from flask_sqlalchemy import SQLAlchemy             # pylint: disable=import-error
from flask_cors import CORS                           # pylint: disable=import-error

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite database URI
db = SQLAlchemy(app)
CORS(app)  # Enable CORS for cross-origin requests

if __name__ == '__main__':
    app.run(debug=True)
