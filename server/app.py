from flask import Flask, request, jsonify
from models import db, User, Post, Tag

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DEBUG = True #Enabling debugging mode

db.init_app(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    # SerializerMixin's to_dict() handles JSON conversion automatically
    return jsonify([user.to_dict() for user in users])

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port = 5555)
