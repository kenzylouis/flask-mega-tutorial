## Module 3

0. Prequisites 
Module-2
<br>

1. Install Flask-WTF
```shell
pip install flask-wtf
```
2. Create a configuration file containing configuration parameter for the app. A very extensible option, is to use a class to store configuration variables.
```shell
touch config.py
```

3. Update `app/__init__.py` to import the Config from the config.py module.
- to verify
```python
python
>>> from app import app
>>> app.config['SECRET_KEY']
xxxxxxxxxxx
>>>
```

4. Create the `app/forms.py` to get manage our form Class. Fields on the Form are Class Variables. Let start with a Login page. the Class LoginForm will extend FlaskForm
```shell
touch app/forms.py
```

5. Create the template for the Login form `app/templates/login.html` that takes form as argument
```shell
touch app/templates/login.html
```
- update `routes.py` to add a login route that will render `login.html`. Import Loginform from form and render it by passing an instance of it. add a link to it in `base.html`.


Next: [module 04](Notes_4.md)