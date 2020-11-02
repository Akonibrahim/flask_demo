from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    names = ["Ibrahim","Sha"]
    return render_template('hello.html',names=names)
