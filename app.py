# A RANDOM NUMBER GENERATING API
# THIS IS JUST ABOUT THE SIMPLEST API SERVER YOU COULD EVER CREATE

from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    randoms = [random.random() for i in range(100)]

    return jsonify(
        {'results':randoms}
    )

    #If you wanted to return HTML instead, simply `return` a string with markup
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
