from flask import Blueprint, request, jsonify
from main import db
from models.medicine import Medicine

# Create a Blueprint instead of using @app
medicine_bp = Blueprint('medicine_bp', __name__)

@medicine_bp.route('/add-medicine', methods=['POST'])
def add_medicine():
    data = request.json
    try:
        new_medicine = Medicine(
            name=data['name'],
            category=data.get('category'),
            price=data.get('price'),
            expiry_date=data.get('expiry_date')
        )
        db.session.add(new_medicine)
        db.session.commit()
        return jsonify({"message": "Medicine added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400