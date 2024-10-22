Image to Speech Converter : 

    This project is a Python Flask web application that allows users to upload an image containing text (written or digitized), extracts the text from the image using Optical Character Recognition (OCR), and converts the extracted text into speech using a Text-to-Speech (TTS) engine.

    Features
        Image Upload: Upload an image containing text.
        Text Extraction: Extract text from the uploaded image using Tesseract OCR.
        Text-to-Speech: Convert the extracted text into an audio file (MP3) using the Google Text-to-Speech (gTTS) API.
        Audio Playback: Play the generated speech audio directly in the browser.


Project Structure : 


image-to-speech/

│

├── app.py                       # Main Flask app

├── static/                      # Folder for static files (images, audio)

│   └── uploads/                 # Store uploaded images and audio files

│

├── templates/                   # HTML templates for the frontend

│   └── index.html               # Main page with upload form

│

├── utils/                       # Utility functions

│   ├── image_processing.py      # Image-to-text extraction logic

│   └── text_to_speech.py        # Text-to-speech conversion logic

│
├── requirements.txt             # Python dependencies

└── README.md                    # Project overview (this file)


