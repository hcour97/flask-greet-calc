# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

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

@app.route('/add')
def add_func():
    """Returns the sum of two params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route('/sub')
def subtract_func():
    """Returns the difference of two params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    
    return str(result)

@app.route('/mult')
def multiply_func():
    """Returns the product of two params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route('/div')
def divide_func():
    """Returns the quotient of two params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<oper>')
def math_func(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations[oper](a,b)

    return str(result)
