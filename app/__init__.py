from flask import Flaskfrom flask import Flask

from flask_sqlalchemy import SQLAlchemyfrom flask_sqlalchemy import SQLAlchemy

import osimport os

from datetime import datetimefrom datetime import datetime



# Initialize Flask application# Initialize Flask application

app = Flask(__name__)app = Flask(__name__)



# Configure SQLite database# Configure SQLite database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Falseapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')



# Initialize database# Initialize database

db = SQLAlchemy(app)db = SQLAlchemy(app)



# Blog post model for plants# Blog post model for plants

class Post(db.Model):class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)    title = db.Column(db.String(100), nullable=False)

    scientific_name = db.Column(db.String(100))    scientific_name = db.Column(db.String(100))

    content = db.Column(db.Text, nullable=False)    content = db.Column(db.Text, nullable=False)

    image_url = db.Column(db.String(500))    image_url = db.Column(db.String(500))

    categories = db.Column(db.String(200))    categories = db.Column(db.String(200))

    references = db.Column(db.Text)    references = db.Column(db.Text)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    source_urls = db.Column(db.Text)  # For storing scraped URLs    source_urls = db.Column(db.Text)  # For storing scraped URLs

    is_ai_generated = db.Column(db.Boolean, default=False)    is_ai_generated = db.Column(db.Boolean, default=False)

    author = db.Column(db.String(100), nullable=False, default='Anonymous')    author = db.Column(db.String(100), nullable=False, default='Anonymous')



from app import routes  # Import routes after app initialization    def __repr__(self):
        return f'<Post {self.title}>'

# Import routes after app initialization to avoid circular imports
from app import routes

# Create database tables
with app.app_context():
    db.create_all()