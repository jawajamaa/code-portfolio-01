from flask import Flask, jsonify, make_response
from flask_restful import Resource

from config import app, db, api

# from models import *

class Home(Resource):

    def get(self):
        response_dict = {
            "message": "tim ryon's photography portfolio"
        }

        return make_response(
                response_dict,
                200
        )
    
api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
