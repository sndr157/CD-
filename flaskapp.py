
# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/api/')
def index():
    return 'Hello, COW!'

@app.route('/api/cow')
def cow():
    return 'MOoooOo MoooooOOoOo!'