from flask import Flask

from config import app
# from flask import Flask, make_response, jsonify
# from flask_migrate import Migrate
# from flask_restful import Resource

# from flask_cors import CORS

# app = Flask(__name__)

# CORS(app)


@app.route('/')
def index():
    return '<h1>Welcome to the Jungle!!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
