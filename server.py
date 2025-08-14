from flask import Flask, request, jsonify
app = Flask(__name__)
latest_pixels = []

@app.route("/post_pixels", methods=["POST"])
def post_pixels():
    global latest_pixels
    latest_pixels = request.get_json().get("pixels", [])
    return jsonify({"message": "Pixels received."})

@app.route("/get_pixels", methods=["GET"])
def get_pixels():
    return jsonify({"pixels": latest_pixels})

# for Railway
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
