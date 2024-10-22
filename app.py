from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from utils.image_processing import extract_text_from_image
from utils.text_to_speech import convert_text_to_speech

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No file uploaded!', 400
        file = request.files['image']
        if file.filename == '':
            return 'No selected file!', 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from the uploaded image
        extracted_text = extract_text_from_image(filepath)
        
        # Convert text to speech and save the output
        audio_file = convert_text_to_speech(extracted_text)

        return redirect(url_for('play_audio', audio_file=audio_file))
    
    return render_template('index.html')

@app.route('/play/<audio_file>')
def play_audio(audio_file):
    return f'<audio controls><source src="/static/uploads/{audio_file}" type="audio/mp3"></audio>'

if __name__ == '__main__':
    app.run(debug=True)
