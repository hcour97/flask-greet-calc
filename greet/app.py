## ROOT ROUTE
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    """Display Homepage"""

    return """
    <html>
        <body>
        <h1>Welcome to My Homepage!</h1>
        </body>
    </html>
    """

@app.route('/welcome')
def welcome():
    """Displays Welcome Page"""

    return f"<h1>Welcome</h1>"

@app.route('/welcome/home')
def welcome_home():
    """Displays Welcome Home Page"""

    return f"<h1>Welcome Home</h1>"

@app.route('/welcome/back')
def welcome_back():
    """Displays Welcome Home Page"""

    return f"<h1>Welcome Back</h1>"