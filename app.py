from flask import Flask
from bd import chars


app = Flask(__name__)


@app.route('/chars', methods = ['GET'])
def get_chars():
    return chars
     
app.run( debug = True)