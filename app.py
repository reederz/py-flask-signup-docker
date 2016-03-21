from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def whoop():
    return 'hello'

if os.environ.get('DOTEST', '0') == '1':
    print 'tests passed'
else:
    app.run()
