#!/usr/bin/env python3

from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print to console
    return param

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param + 1))  # Adjust range
    return f'<h2>Count Numbers:</h2><pre>{numbers}</pre>'

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h2>Error: Division by zero</h2>'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return '<h2>Error: Modulo by zero</h2>'
    else:
        return '<h2>Error: Invalid operation</h2>'

    return f'<h2>Math Result: {num1} {operation} {num2} = {result}</h2>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
