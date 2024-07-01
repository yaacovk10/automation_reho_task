from flask import Flask, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)

def get_current_utc_iso_format():
    return datetime.now(timezone.utc).isoformat()

# Sample data to simulate a database
users = [
     {
        'id': 1,
        'email': 'george.bluth@reqres.in',
        'first_name': 'George',
        'last_name' :'Bluth' ,
        'createdAt':  get_current_utc_iso_format(),
        'updatedAt':  get_current_utc_iso_format(),
        'avatar': 'https://reqres.in/img/faces/1-image.jpg'
    },
    {
        'id': 2,
        'email': 'janet.weaver@reqres.in',
        'first_name': 'Janet',
        'last_name' :'Weaver',
        'createdAt':  get_current_utc_iso_format(),
        'updatedAt':  get_current_utc_iso_format(),
        'avatar': 'https://reqres.in/img/faces/2-image.jpg'
    },
    {
        'id': 3,
        'email': 'tsion.israeli@reqres.in',
        'first_name': 'Tsion',
        'last_name' :'Israeli',
        'createdAt':  get_current_utc_iso_format(),
        'updatedAt':  get_current_utc_iso_format(),
        'avatar': 'https://reqres.in/img/faces/3-image.jpg'
    }
]


# Utility function for pagination
def paginate(items, page, per_page):
    total = len(items)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_items = items[start:end]
    total_pages = (total + per_page - 1) // per_page  # ceiling division
    return {
        'page': page,
        'per_page': per_page,
        'total': total,
        'total_pages': total_pages,
        'data': paginated_items
    }

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 6))
    paginated_data = paginate(users, page, per_page)
    return jsonify(paginated_data)

# GET a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    required_fields = ['first_name', 'last_name', 'email']
    
    # Check if all required fields are present
    if not all(field in new_user for field in required_fields):
        return jsonify({'message': 'Invalid user data'}), 400

    new_user['id'] = users[-1]['id'] + 1 if users else 1
    current_time = get_current_utc_iso_format()
    new_user['createdAt'] = current_time
    new_user['updatedAt'] = current_time
    users.append(new_user)
    return jsonify(new_user), 201

# PUT (update) a user's details
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    data = request.get_json()
    user.update(data)
    user['updatedAt'] =  get_current_utc_iso_format(),
    return jsonify(user)



# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 200



if __name__ == '__main__':
    app.run(debug=True)