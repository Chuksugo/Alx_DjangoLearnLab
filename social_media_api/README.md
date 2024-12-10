Social Media API
A Social Media API built with Django and Django REST Framework (DRF). This API provides user registration, authentication, and profile management functionality.

Setup Guide
Clone the Repository
Clone the repository to your local machine.

Set Up a Virtual Environment
Create and activate a virtual environment.

Install Dependencies
Install the required Python packages.

Configure the Database
Update the database settings in settings.py to match your database configuration.

Run Migrations
Apply database migrations to set up the required tables.

Start the Development Server
Run the server to begin using the API.

User Registration and Authentication
Register: Users can register by providing a username, password, and email.
Login: Users can log in to obtain an authentication token.
Authentication: Use the token in the Authorization header to access protected endpoints.
User Model Overview
The project includes a custom user model with the following fields:

Profile Picture: An image field for the user's profile picture.
Bio: A short bio or description of the user.
Followers: A ManyToMany field for user follow relationships.
This custom user model extends Django's built-in user model to support additional attributes and features for better profile management.

