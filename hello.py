from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p> <img src="https://images.pexels.com/photos/617278/pexels-photo-617278.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"></img>' 
