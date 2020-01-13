from flask import Flask, request, Response, send_file
from flask_restful import Resource, Api

from AI.assess_image import assess_image


app = Flask(__name__)
api = Api(app)


class Upload(Resource):

  def post(self):

    img = request.files["media"]
    
    if assess_image(img):
      return Response(status = 200)
    
    return Response(status = 501)


class Output(Resource):

  def post(self):

    return send_file("AI/process_data/output_image.jpg", as_attachment = True)



class Report(Resource):

  def post(self):

    return send_file("AI/process_data/report.json", as_attachment = True)
  


api.add_resource(Upload, "/upload")
api.add_resource(Output, "/output")
api.add_resource(Report, "/report")


if __name__ == "__main__":
  app.run(debug = True)
