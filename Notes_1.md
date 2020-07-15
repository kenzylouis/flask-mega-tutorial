
0. Prerequisites
Install flask

```shell
### on Mac 
virtualenv -p /Library/Frameworks/Python.framework/Versions/3.8/bin/python3 .venv
source .venv/bin/activate
pip install flask
```
1. create a an app directory and create the __init__.py
```shell
mkdir app
cd app
touch __init__.py
```
2. create the routes.py file under the app folder
```shell
touch routes.py
```
3. To complete the application, you need to have a Python script at the top-level that defines the Flask application instance.
```shell
## go back one directory up
cd ..
touch blog.py
```
4. Before running the app, Flask needs to be told how to import it, by setting the FLASK_APP environment variable:
```shell
export FLASK_APP=blog.py
```
5. Flask allows you to register environment variables that you want to be automatically imported when you run the flask command. we can do this with the `python-dotenv` module
```shell
pip install python-dotenv
```
6. create a .flaskenv and put the `FLASK_APP` env variable in it
```shell
touch .flaskenv
```