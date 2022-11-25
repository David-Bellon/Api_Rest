from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        df = pd.read_csv("user.csv")
        data = df.to_dict()
        return {"data": data}, 200
    

    def post(self):
        df = pd.read_csv("user.csv")
        parser = reqparse.RequestParser()

        parser.add_argument("userId", required=True)
        parser.add_argument("name", required=True)
        parser.add_argument("city", required=True)

        args = parser.parse_args()

        if args["userId"] in list(df["userId"]):
            return {
                "message": f"ERROR. {args['userId']} already exist"
            }, 401
        else:
            aux = pd.DataFrame({
                "userId": args["userId"],
                "name": args["name"],
                "city": args["city"],
                "locations": [[]]
            })

            
            pd.concat([df, aux])
            df.to_csv("user.csv", index=False)

            return {"data", df.to_dict()}, 200

class Locations(Resource):
    def get(self):
        df = pd.read_csv("locations.csv")
        data = df.to_dict()
        return {"data": data}, 200

    def post(self):
        pass

api.add_resource(Users, "/users")
api.add_resource(Locations, "/locations")



if __name__ == "__main__":
    app.run()