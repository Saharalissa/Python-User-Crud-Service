## User Management CRUD Server

This project is a Python-based CRUD (Create, Read, Update, Delete) server for managing user data.
It includes endpoints for basic user management with `username`, `password`, and `active` status fields.


---

## Features
- **Create** a new user.
- **Read** all users or a specific user.
- **Update** user details.
- **Delete** a user.
- **Separation of Concerns**: Modularized into routes, controllers, and configuration files.

---

## Technologies
- **Backend**: Flask
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Configuration Management**: `dotenv`

---
## Project Installation
After cloning the repo, Install Dependencies, run **pip install -r requirements.txt**


## Set Up Environment Variables
Create a .env file in the project root and add the following:

DB_USERNAME=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=userTest

## Run the Application
python app.py

## API Endpoints
Base URL
http://localhost:5000

Method Endpoint Description
POST    /users	    Create a new user
GET	    /users	    Get all users
GET	    /users/<id>	Get user by ID
PUT	    /users/<id>	Update user by ID
DELETE	/users/<id>	Delete user by ID

## Testing with Postman
Import the API endpoints into Postman. e.g.  GET localhost:5000/users

## Example on create User

POST /users
Content-Type: application/json
{
  "username": "Sahar",
  "password": "password",
  "active": True
}