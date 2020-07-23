### Module 5

### 0. Prerequisites
Module-4

### 1. Password Hashing
update models.py with 2 method to set and get password hashing

### 2. Install Flask-Login
Install the `flask-login` extension:
```shell
pip install flask-login
```

### 3. initialize Flask-Login like other extensions
Flask-Login needs to be created and initialized right after the application instance in `app/__init__.py`. Use LoginManager.


### 4. Create Model for Flask-Login
Flask loging need these 4 attribute and methods:
`is_authenticated`, `is_active`, `is_anonymous`,` get_id()` respectively  to  check if a user is login, to check if an account is valid, to check if it is am unknown user, to return a unique identifier of user.
- All these  are implemented in Flask-Login in a class called `UserMixin` 
- Add UserMixin in models.py

### 5. User session
create in models a `user_load()` function to get the user id in order to manage the user session. It is registered to Flask Login  via a decorator

### 6. Create the route for login
Update `routes.py` and add the logic for login



