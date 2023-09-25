from flask import Flask,request, jsonify

app = Flask(__name__)
data = {}

@app.route("/")
def index():
    return "Welcome to the app"

@app.route("/post", method = ["POST"])
def postCreate():
    data = request.json
    username = data["username"]
    caption = data["caption"]
    resData = {
        "message" : f"{username} and {caption} posted"
    }

    return resData

if __name__ == "__main__":
    app.run(debug=True)
