from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Pharmacy Backend Running 🚀"

# Import routes
import routes.medicine_routes

if __name__ == '__main__':
    app.run(debug=True)
