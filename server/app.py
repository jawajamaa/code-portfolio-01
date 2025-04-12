
from flask import Flask, jsonify, make_response
from flask_restful import Resource
import pymupdf

# from pdfminer.layout import LAParams
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from pdfminer.layout import LTTextBoxHorizontal


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
        doc = pymupdf.open("./client/public/documents/Ryon-Timothy-A-Little-About-Me.pdf")
        out = open("output.txt", "wb")

        try:
            for page in doc:
                # print(f"Line 38 app.py AboutMe text as follows: {aboutMe}")
                text = page.get_text("blocks", sort = True).encode("utf8")
                out.write(text)
                out.write(bytes((12,)))
            out.close()
            
        except Exception as exc:
            return jsonify({'error': str(exc)}), 500

        response = make_response(out, 200)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    
#     def get(self):
#         lines = list()

#         try:
#             with open('../client/public/documents/Ryon-Timothy-A-Little-About-Me.pdf') as aboutMe:
#                 print("Line 38 app.py AboutMe text as follows:", aboutMe)
#             # no print statement in cli, so doesn't work? try in cli first?

#                 # return lines
            
#         except Exception as exc:
#             print(f"File {aboutMe} cannot be opened")
#             return jsonify({'error': str(exc)}), 500
# # getting ValueError on line 47 - 'I/O operation on closed file'
#         for line in aboutMe:
#             lines.append(line)
#         # text_response =
#         response = make_response(lines, 200)
#         # response = make_response(text_response, 200)
#         response.headers.add("Access-Control-Allow-Origin", "*")
#         return response
    
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
