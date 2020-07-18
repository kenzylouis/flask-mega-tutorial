
## Module 1

#### 0. Prerequisites
Install flask

```shell
### on Mac 
virtualenv -p /Library/Frameworks/Python.framework/Versions/3.8/bin/python3 .venv
source .venv/bin/activate
pip install flask
```
#### 1. Create the app in the root folder
create an app directory and create the __init__.py
```shell
mkdir app
cd app
touch __init__.py
```
#### 2. Create a route for the views
Create the routes.py file under the app folder
```shell
touch routes.py
```
#### 3. Entrypoint of the app
To complete the application, you need to have a Python script at the top-level that defines the Flask application instance.
```shell
## go back one directory up
cd ..
touch blog.py
```
#### 4. Environment variable
Before running the app, Flask needs to be told how to import it, by setting the FLASK_APP environment variable:
```shell
export FLASK_APP=blog.py
```
#### 5. Flask environment variable
Flask allows you to register environment variables that you want to be automatically imported when you run the flask command. we can do this with the `python-dotenv` module
```shell
pip install python-dotenv
```
#### 6. The `.flaskenv` file
create a .flaskenv and put the `FLASK_APP` env variable in it
```shell
touch .flaskenv
```

Next: [module 02](Notes_2.md)