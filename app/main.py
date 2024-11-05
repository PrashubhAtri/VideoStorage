from flask import Flask, render_template, request, redirect, url_for
from app.utils import read_file, ascii_to_rgb, create_frames, create_video
import os

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Ensure the uploads directory exists
            upload_folder = 'uploads'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)
            
            # Process the file
            content = read_file(file_path)
            rgb_values = ascii_to_rgb(content)
            frames = create_frames(rgb_values)
            create_video(frames, output_path='static/output.avi')
            
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
