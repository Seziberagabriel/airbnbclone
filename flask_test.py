from flask import *

# GOALS for the MATH API:
# 1. Create the root route that displays a welcome message and the available routes - DONE
# 2. Create a route that returns the sum of two numbers - DONE
#   2.1. Get the numbers from the URL as query parameters - DONE
#   2.2. Return the result in json ({operands: [a, b], operator: '+', result: a + b}) - DONE
# 3. Create a route that returns the product of two numbers - DONE
# 4. Create a route that returns the difference of two numbers
# 5. Create a route that returns the quotient of two numbers



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum')
def sum():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return jsonify({'operands': [a, b], 'operator': '+', 'result': a + b})

@app.route('/product')
def product():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return jsonify({'operands': [a, b], 'operator': '*', 'result': a * b})

@app.route('/subtract')
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return jsonify({'operands': [a, b], 'operator': '-', 'result': a - b})

@app.route('/divide')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return jsonify({'operands': [a, b], 'operator': '/', 'result': a / b})


if __name__ == '__main__':
    app.run(debug=True)