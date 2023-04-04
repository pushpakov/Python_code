# InstaLike App

InstaLike is a simple Flask app that simulates a social media platform where users can follow each other and view their followers.

## Getting Started

1. Clone the repository: `git clone https://github.com/username/InstaLike.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Access the app on your browser at `http://localhost:5000`

## Endpoints

- `/add` - Add a new user (POST)
- `/users` - Get all users (GET)
- `/users/<id>` - Get a user by ID (GET)
- `/delete/<id>` - Delete a user by ID (DELETE)
- `/update/<id>` - Update a user by ID (PUT)
- `/follow` - Add a follower to a user (POST)
- `/followers/<user_id>` - Get all followers for a user (GET)

<!-- implement logging, model package for data class, db package for database operations and use environment variable for configuring the credentials   --> 

