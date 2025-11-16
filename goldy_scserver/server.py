from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import secrets
from typing import Tuple

class Config:
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    SCREENSHOT_DIR: str = "screenshots"
    ALLOWED_EXTENSIONS: Tuple[str, ...] = ("jpg", "jpeg", "png")

os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)

def generate_filename(extension: str = "jpg") -> str:
    token = secrets.token_hex(12)
    return f"{token}.{extension}"

def allowed_file(filename: str) -> bool:
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    )

app = Flask(__name__)
CORS(app)

@app.post("/upload_screenshot")
def upload_screenshot():
    if "files[]" not in request.files:
        return jsonify(success=False, error="File not found"), 400
    
    uploaded = request.files["files[]"]

    if uploaded.filename == "":
        return jsonify(success=False, error="File name is empty"), 400

    if not allowed_file(uploaded.filename):
        return jsonify(success=False, error="Unsupported file format"), 415

    ext = uploaded.filename.rsplit(".", 1)[1].lower()
    filename = generate_filename(ext)
    filepath = os.path.join(Config.SCREENSHOT_DIR, secure_filename(filename))

    uploaded.save(filepath)

    return jsonify(success=True, filename=filename), 201


@app.get("/screenshot/<path:filename>")
def screenshot(filename: str):
    return send_from_directory(Config.SCREENSHOT_DIR, filename)
    

if __name__ == "__main__":
    print("=" * 60)
    print("           GOLDY SCREENSHOT SERVER ")
    print("=" * 60)
    print(f" Server running at: http://{Config.HOST}:{Config.PORT}")
    print(f" Screenshot folder: {Config.SCREENSHOT_DIR}")
    print("=" * 60)

    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=False,
        threaded=True
    )
