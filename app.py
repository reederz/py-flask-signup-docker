from flask import Flask

app = Flask(__name__)

@app.route('/')
def whoop():
    return 'hello'

app.run()
