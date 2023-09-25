from flask import Flask,request, jsonify

app = Flask(__name__)
data = []
postId = 1

def createPost(username,caption):
    global postId
    post = {"id" :postId, "username" : username, "caption" : caption }
    data.append(post)
    postId+=1

@app.route("/")
def index():
    return "Welcome to the app"




@app.route("/post", methods = ["POST"])
def postCreate():
    data = request.json
    username = data["username"]
    caption = data["caption"]
    createPost(username,caption)
    return jsonify ({"message" : f"{username} and {caption} posted"})

if __name__ == "__main__":
    app.run(debug=True)
