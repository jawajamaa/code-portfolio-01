from flask import make_response
from flask_restful import Resource

from config import app, db, api

from models import Code, Image, PopQuiz

class Home(Resource):

    def get(self):
        response_dict = {
            "message": "tim ryon's website"
        }

        return make_response(
                response_dict,
                200
        )
    
api.add_resource(Home, '/')

class CodeFiles(Resource):

    def get(self):
        response_dict = {
            "message" : "tim ryon's code files"
        }

        return make_response(
            response_dict,
            200
        )
    
api.add_resource(CodeFiles, '/codefiles')

class ImageFiles(Resource):

    def get(self):
        image_response = [img.to_dict() for img in Image.query.all()]
        response = make_response(image_response, 200)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    
api.add_resource(ImageFiles, '/imagefiles')

class QuizFiles(Resource):

    def get(self):
        response_dict = {
            "message" : "tim ryon's PopQuiz files"
        }

        return make_response(
            response_dict,
            200
        )
    
api.add_resource(QuizFiles, '/quizfiles')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
