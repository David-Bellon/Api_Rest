from flask import Flask, request
import pandas as pd
app = Flask(__name__)

@app.route("/users", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        df = pd.read_csv("user.csv")
        data = df.to_dict()
        return {"data": data}, 200
    
    if request.method == "POST":
        df = pd.read_csv("user.csv")

        args = dict(request.args)

        if args["locations"] == "None":
            locations = []
        else:
            aux = args["locations"].split("[")[1].split("]")[0].split("'")
            locations = []
            for i in range(len(aux)):
                if i % 2 == 1:
                    locations.append(aux[i])

        if args["userId"] in list(df["userId"]):
            return {
                "message": f"ERROR. {args['userId']} already exist"
            }, 401
        else:
            aux = pd.DataFrame({
                "userId": args["userId"],
                "name": args["name"],
                "city": args["city"],
                "locations": [locations]
            })

            
            df = pd.concat([df, aux], ignore_index=True)
            df.to_csv("user.csv", index=False)

            return {"data": df.to_dict()}, 200



if __name__ == "__main__":
    app.run()