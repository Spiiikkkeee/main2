from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    try:

        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

        download_path = stream.download(output_path="downloads")
        filename = os.path.basename(download_path)

        return send_file(download_path, as_attachment=True, download_name=filename)
    except Exception as e:
        return f"An error occurred: {str(e)}"
    

    if __name__ == '__main__':

        os.makedirs("downloads", exist_ok=True)
        app.run(debug=True)
