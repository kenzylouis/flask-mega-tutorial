from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'kenzy'}
    posts = [
        { 
            'author': {'username':'John'},
            'body': 'It is a beautiful day in the neighborhood!'
        
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)