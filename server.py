from flask import Flask, request, jsonify

app = Flask(__name__)
latest_frame = b""
latest_width = 0
latest_height = 0

@app.route("/post_pixels", methods=["POST"])
def post_pixels():
    global latest_frame, latest_width, latest_height
    latest_frame = request.data
    latest_width = int(request.args.get("w", 0))
    latest_height = int(request.args.get("h", 0))
    return "ok", 200

@app.route("/get_pixels", methods=["GET"])
def get_pixels():
    return latest_frame, 200, {
        "Content-Type": "application/octet-stream",
        "X-Width": str(latest_width),
        "X-Height": str(latest_height),
    }

# Render requires port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
