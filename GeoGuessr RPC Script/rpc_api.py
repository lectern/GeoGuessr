from flask import Flask
from flask_restful import Resource, Api, reqparse

# reference: https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f

app = Flask(__name__)
api = Api(app)

title = ""

class RPC(Resource):
    def get(self):
        return {'data': title}, 200
    
    def post(self):
        global title
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        
        args = parser.parse_args()
        title = args['title']

        return {}, 200

@app.after_request
def handle_options(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"

    return response

api.add_resource(RPC, '/rpc')

if __name__ == "__main__":
    app.run()