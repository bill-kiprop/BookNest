from flask import Flask, request, jsonify
from app_init import db
from app.models import User, Property, Review
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to your actual secret key
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email, password_hash=password).first()
    if not user:
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity={'email': user.email, 'role': user.role})
    return jsonify(access_token=access_token), 200

@app.route('/properties', methods=['POST'])
@jwt_required()
def add_property():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()

    if user.role != 'host':
        return jsonify({"msg": "Permission denied"}), 403

    new_property = Property(
        name=data['name'],
        description=data['description'],
        address=data['address'],
        host_id=user.id
    )
    db.session.add(new_property)
    db.session.commit()
    return jsonify({"msg": "Property created successfully!"}), 200

@app.route('/properties/<int:id>', methods=['PUT'])
@jwt_required()
def edit_property(id):
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()

    property = Property.query.get(id)
    if property.host_id != user.id:
        return jsonify({"msg": "Permission denied"}), 403

    property.name = data.get('name', property.name)
    property.description = data.get('description', property.description)
    property.address = data.get('address', property.address)

    db.session.commit()
    return jsonify({"msg": "Property updated successfully!"}), 200

@app.route('/properties/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_property(id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()

    property = Property.query.get(id)
    if property.host_id != user.id:
        return jsonify({"msg": "Permission denied"}), 403

    db.session.delete(property)
    db.session.commit()
    return jsonify({"msg": "Property deleted successfully!"}), 200

@app.route('/reviews', methods=['POST'])
@jwt_required()
def add_review():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()

    new_review = Review(
        content=data['content'],
        rating=data['rating'],
        user_id=user.id,
        property_id=data['property_id']
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"msg": "Review added successfully!"}), 200

@app.route('/reviews/<int:id>', methods=['PUT'])
@jwt_required()
def edit_review(id):
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()

    review = Review.query.get(id)
    if review.user_id != user.id:
        return jsonify({"msg": "Permission denied"}), 403

    review.content = data.get('content', review.content)
    review.rating = data.get('rating', review.rating)

    db.session.commit()
    return jsonify({"msg": "Review updated successfully!"}), 200

@app.route('/reviews', methods=['GET'])
def display_reviews():
    reviews = Review.query.all()
    reviews_list = [{"content": r.content, "rating": r.rating, "user_id": r.user_id, "property_id": r.property_id} for r in reviews]
    return jsonify(reviews_list), 200

if __name__ == '__main__':
    app.run(debug=True)
