from flask import Flask
from models import db, User
from config import Config
from router import user_bp 

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Initialize DB
# Create Database If does not exist
with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(user_bp)

# Initialize the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
