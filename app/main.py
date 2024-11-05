from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Process the file and convert to video
            # {{ process_file_to_video(file) }}
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
