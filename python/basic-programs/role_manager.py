"""
This program demonstrates the use of class and instance variables in Python.
The program is a basic role manager that defines a User class with primary and secondary roles.

@author wm00026
"""

"""
User class:
Defines a user with primary and secondary roles, email, and password.

Self variables:
- role: specific role assigned to the user
- email: user's email address
- password: user's password
"""

class User:
    """
    @brief Constructor to intiialize the User object with role rolel, email, and password.
    @param self - instance of the class (required for python)
    @param role - String - the secondary role of the user (Admin, Moderator)
    @param email - String - the email of the user
    @param password - String - the password of the user
    """
    def __init__ (self, role, email, password):
        self.role = role
        self.email = email
        self.password = password

    """
    function display_info
    @brief: Displays the user's primary and secondary roles, email, and password.
    @param self - instance of the class (required for python)
    """
    def display_info(self):
        print(f"Role: {self.role}")
        print(f"Email: {self.email}")

# Main program
if __name__ == "__main__":
    # Create a User instance with primary role 'User' and secondary role 'Admin'
    user1 = User(role="Admin", email="", password="")
    user2 = User(role="Moderator", email="", password="")
    user1.email="email@email.com"
    user1.password = "admin123"
    user2.password = "moderator123"
    user2.email="funemail@thefunnestemail.org"

    user1.display_info()
    user2.display_info()