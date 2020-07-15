from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'kenzy'}
    return """
        <html>
            <head>
                <title>Home - My Blog</title>
            </head>
            <body>
                <h2>Hello, """ + user['username'] + """!!</h2>
            </body>
        </html>
    """