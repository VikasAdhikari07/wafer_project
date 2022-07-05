from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/factorial/<int:n>')
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return str(fact)

if __name__ == "__main__":
    app.run(debug=True)