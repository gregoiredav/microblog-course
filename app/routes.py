from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'gregoire'}
    posts = [
        {
            'author': {'username': 'gregoire'},
            'body': 'vous êtes une vieille crotte'
        },
        {
            'author': {'username': 'crotte'},
            'body': 'Oh oui!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
