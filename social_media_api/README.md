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



======


 Enhance the CustomUser model to support user follow relationships and feed functionality.

Model Updates:

Added Fields:
followers: A ManyToManyField representing users who follow the current user, with a related_name='followed_by'.
following: A ManyToManyField representing users the current user is following, with a related_name='following_users'.
Migration:

Run the following commands to update the database schema:
bash
Copy code
python manage.py makemigrations accounts
python manage.py migrate
Functionality:

Follow/Unfollow: Users can follow or unfollow other users, creating a bidirectional relationship.
Accessing Relationships:
user1.following.add(user2) to follow another user.
user1.following.remove(user2) to unfollow.
user2.followed_by.all() to see who follows user2.
user1.following_users.all() to see whom user1 is following.
Future Considerations:

Ensure consistency in relationship handling.
Use descriptive related_name attributes for readability.
Consider edge case handling, such as preventing self-following or duplicate entries.
These updates provide the foundation for user interactions related to following, unfollowing, and generating feeds based on users’ follow relationships.


### **API Endpoint Documentation Summary**

1. **Like Post Endpoint** (`POST /posts/<int:post_id>/like/`):
   - Allows users to like a post.
   - Returns a success message and generates a notification.
   - Prevents users from liking a post multiple times.

2. **Unlike Post Endpoint** (`POST /posts/<int:post_id>/unlike/`):
   - Allows users to unlike a post.
   - Removes the like and generates an unlike notification.

3. **View Notifications Endpoint** (`GET /notifications/`):
   - Retrieves a list of notifications for the authenticated user.
   - Displays notifications with details like the actor, recipient, and the post.

---

### **Testing Results Summary**

1. **Like Post**: Verified that a user can like a post and a notification is generated.
2. **Prevent Multiple Likes**: Ensured a user cannot like the same post multiple times.
3. **Unlike Post**: Confirmed users can unlike a post, removing the like and generating an unlike notification.
4. **View Notifications**: Ensured that notifications are displayed correctly for the user.

All tests passed successfully, confirming the like and notification features work as intended.