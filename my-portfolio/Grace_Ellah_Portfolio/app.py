
from flask import Flask, send_from_directory, render_template
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=None)

@app.route("/")
def home():
    index_file = os.path.join(BASE_DIR, "index.html")

    if os.path.isfile(index_file):
        return send_from_directory(BASE_DIR, "index.html")

    template_file = os.path.join(BASE_DIR, "templates", "index.html")

    if os.path.isfile(template_file):
        return render_template("index.html")

    return "ERROR: index.html not found. Check your project directory.", 404


@app.route("/<path:filename>")
def serve_files(filename):
    return send_from_directory(BASE_DIR, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
