# from docx import Document
from flask import Flask, jsonify, make_response
from flask_restful import Resource
# from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal


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
        lines = list()

        try:
            with open('../client/public/documents/Ryon-Timothy-A-Little-About-Me.pdf') as aboutMe:
                print("Line 28 app.py AboutMe text as follows:", aboutMe)
            # no print statement in cli, so doesn't work? try in cli first?

                # return lines
            
        except Exception as exc:
            print(f"File {aboutMe} cannot be opened")
            return jsonify({'error': str(exc)}), 500
# getting ValueError on line 47 - 'I/O operation on closed file'
        for line in aboutMe:
            lines.append(line)
        # text_response =
        response = make_response(lines, 200)
        # response = make_response(text_response, 200)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

# line 59 would start after lines = list(), but doesn't appear to works
        # with open('../client/public/documents/Ryon-Timothy-A-Little-About-Me.pdf') as aboutMe:
        #     print("Line 28 app.py AboutMe text as follows:", aboutMe)
        #     # no print statement in cli, so doesn't work? try in cli first?
        #     try:
        #         resourceMgr = PDFResourceManager()
        #         laparams = LAParams()
        #         device = PDFPageAggregator(resourceMgr, laparams=laparams)
        #         interpreter = PDFPageInterpreter(resourceMgr, device)
                
        #         for page in PDFPage.get_pages(aboutMe):
        #             interpreter.process_page(page)
        #             layout = device.get_result()

        #             for element in layout:
        #                 if isinstance(element, LTTextBoxHorizontal):
        #                     lines.extend(element.get_text().splitlines())

        #         return lines
            
        #     except Exception as exc:
        #         return jsonify({'error': str(exc)}), 500

# in place of above try statement
            # try:
            #     aboutMePdfText = extract_text(aboutMe)
            #     return jsonify(aboutMePdfText)
            #     # return jsonify({'text': aboutMePdfText})
            # except Exception as exc:
            #     return jsonify({'error': str(exc)}), 500

        # return make_response(
        #     response_dict,
        #     200
        # )

    # def get(self):
    #     meDoc = Document("../client/public/documents/20241017_A-Little-About-Me-json-form.json")
    #     full_text = []
    #     for para in meDoc.paragraphs:
    #         full_text.append('  ' + para.text)
    #     response_dict = '\n\n'.join(full_text)
# getting error that text when receiveing the fetch is not 'valid Json' - due to it not being an array of objects most likely?  refactor code here to return a list of dictionaries where each paragraph is another dictionary within the main list, thereby making it valid json?  ie. [{para1: "lorem ipsum"}, {para2: "lorem ipsum"}] etc.


        # return make_response(
        #     response_dict,
        #     200
        # )
    
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
