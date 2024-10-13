from docx import Document
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

class AboutMeFiles(Resource):

    def get(self):
        meDoc = Document("../client/public/documents/20241010_A-Little-About-Me.docx")
        full_text = []
        for para in meDoc.paragraphs:
            full_text.append('  ' + para.text)
        response_dict = '\n\n'.join(full_text)
# getting error that text when receiveing the fetch is not 'valid Json' - due to it not being an array of objects most likely?  refactor code here to return a list of dictionaries where each paragraph is another dictionary within the main list, thereby making it valid json?  ie. [{para1: "lorem ipsum"}, {para2: "lorem ipsum"}] etc.


        return make_response(
            response_dict,
            200
        )
    
api.add_resource(AboutMeFiles, '/aboutmefiles')

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
