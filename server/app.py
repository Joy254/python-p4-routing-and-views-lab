#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/math', methods=['POST'])
def math():
    try:
        num1 = float(request.form['num1'])
        operation = request.form['operation']
        num2 = float(request.form['num2'])

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

    except ValueError:
        return '<h2>Error: Invalid input. Please provide valid numbers.</h2>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
