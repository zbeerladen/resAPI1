from flask import Flask
from flask_restful import Resource, Api

app = Flask("VideoAPI")
api = Api(app)


class Video(Resource):

    def get(selfs):
        return "Hello World"

api.add_resource(Video, '/')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
