# User Management REST API
This project is a simple User Management REST API built using Flask. It provides endpoints to manage user data, including creating, retrieving, updating, and deleting users. Each user has fields such as first_name, last_name, email, avatar, createdAt, and updatedAt.

## Features
GET /users: Retrieve all users with pagination.
GET /users/<id>: Retrieve a specific user by ID.
POST /users: Create a new user.
PUT /users/<id>: Update an existing user.
DELETE /users/<id>: Delete a user by ID.
## Setup
### Prerequisites
Ensure you have Python 3.x and pip installed on your machine.

### Installation
#### 1. Clone the Repository:
```
git clone <path on github>
```

#### 2. Create and Activate a Virtual Environment (optional but recommended):
```
python -m venv myvenv
myvenv\Scripts\activate`
```
#### 3. Install Dependencies:
```
pip install -r requirements.txt
```

## Running the API
#### 1. Start the Flask Server:
```
python app.py
```
The API will be available at http://127.0.0.1:5000.

## API Endpoints
* __GET /users__

    * Retrieve a list of users with pagination support.
    * Query Parameters: page (optional), per_page (optional)
    * Response Example:
            ```
            {
        "page": 1,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": [
            {
            "id": 1,
            "first_name": "George",
            "last_name": "Bluth",
            "email": "george.bluth@reqres.in",
            "avatar": "https://reqres.in/img/faces/1-image.jpg",
            "createdAt": "2024-07-01T10:00:00Z",
            "updatedAt": "2024-07-01T10:00:00Z"
            },
            
        ]
        }

            ```

* __GET /users/\<id\>__
    * Retrieve a specific user by ID.
    * Response Example:

        ```
            {
        "id": 1,
        "first_name": "George",
        "last_name": "Bluth",
        "email": "george.bluth@reqres.in",
        "avatar": "https://reqres.in/img/faces/1-image.jpg",
        "createdAt": "2024-07-01T10:00:00Z",
        "updatedAt": "2024-07-01T10:00:00Z"
        }
        ```

* __POST /users__
    * Create a new user.
    * Request Body Example:
        ```
        {
        "first_name": "Alice",
        "last_name": "Baba",
        "email": "alice.baba@reqres.in",
        "avatar": "https://reqres.in/img/faces/4-image.jpg"
        }
        ```
    * Response Example:
        ```
        {
        "id": 5,
        "first_name": "Alice",
        "last_name": "Baba",
        "email": "alice.baba@reqres.in",
        "avatar": "https://reqres.in/img/faces/4-image.jpg",
        "createdAt": "2024-07-01T10:00:00Z",
        "updatedAt": "2024-07-01T10:00:00Z"
        }
        ```

* __PUT /users/<id>__
    * Update an existing user.
    * Request Body Example:
        ```
        {
        "first_name": "Alice",
        "last_name": "Updated",
        "email": "alice.updated@reqres.in",
        "avatar": "https://reqres.in/img/faces/4-image.jpg"
        }
        ```
    * Response Example:
        ```
        {
        "id": 1,
        "first_name": "Alice",
        "last_name": "Updated",
        "email": "alice.updated@reqres.in",
        "avatar": "https://reqres.in/img/faces/4-image.jpg",
        "createdAt": "2024-07-01T10:00:00Z",
        "updatedAt": "2024-07-01T10:30:00Z"
        }
        ```
* __DELETE /users/<id>__
    * Delete a user by ID.
    * Response Example:
    ```
    {
    "message": "User deleted"
    }
    ```

## Running Unittests
This project includes unittests to validate the functionality and robustness of the API. The tests cover both positive and negative scenarios for all endpoints.

### Running the Tests
#### 1. Ensure the Flask Server is Running:
Make sure the server is running in one terminal window.
```
python app.py
```
#### 2. Run Tests:
In another terminal window, navigate to the project directory and run:
```
python test_api.py
```

### Test Descriptions
* Positive Tests: Verify that the API correctly handles valid requests.
* Negative Tests: Verify that the API properly handles invalid requests or conditions.
### Example Test Cases
* GET /users:

    * Positive: Retrieve all users and validate the response structure and pagination.
    * Negative: Attempt to retrieve users from a non-existent page.

* GET /users/<id>:

    * Positive: Retrieve a user by valid ID and validate the response.
    * Negative: Attempt to retrieve a user by an invalid ID.

* POST /users:

    * Positive: Create a new user with valid data and verify the response.
    * Negative: Attempt to create a user with missing required fields.

* PUT /users/<id>:

    * Positive: Update a user with valid data and verify the response.
    * Negative: Attempt to update a non-existent user.

* DELETE /users/<id>:

    * Positive: Delete a user by valid ID and verify the response.
    * Negative: Attempt to delete a user by an invalid ID.


