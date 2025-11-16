# Goldy Screenshot Server

A lightweight Flask server for handling screenshots from **FiveM**.

## 🚀 Features

- **Receive screenshots** uploaded from clients or FiveM scripts.
- **Store screenshots** in a dedicated folder (`screenshots/`).
- **Serve screenshots** via HTTP for download or preview.
- **Automatic folder creation** if it doesn’t exist.
- **Randomized filenames** for secure and unique storage.
- **CORS enabled** for web or FiveM clients.
- **Minimal dependencies**: Flask, Flask-CORS, Werkzeug.
- **Extensible**: Ready for OCR or other image processing features.


## ⚡ Install dependencies - pip install -r requirements.txt


## ⚙️ Configuration

You can customize the server settings in the `Config` class inside `server.py`. Adjust the values according to your environment and needs:

* **HOST** – The IP address the server will run on. Use `"0.0.0.0"` to allow external connections or `"127.0.0.1"` for local testing only.
* **PORT** – The port number the server will listen on, e.g., `8080`.
* **SCREENSHOT_DIR** – The folder where uploaded screenshots are stored. The server will automatically create this folder if it doesn’t exist.
* **ALLOWED_EXTENSIONS** – A list of allowed file types, e.g., `"jpg", "jpeg", "png"`.

Simply edit these values in `server.py` before running the server to fit your setup.

## 🔑 Usage

```
PerformHttpRequest("http://your-server:8080/upload_screenshot", function(err, text, headers)
    print(text)
end, "POST", data, { ["Content-Type"] = "multipart/form-data" })

{
  "success": true,
  "filename": "a1b2c3d4e5f6.jpg"
}
