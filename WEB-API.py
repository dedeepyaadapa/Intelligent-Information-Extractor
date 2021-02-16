import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import pickle
import pytesseract
import numpy as np 
import cv2 

with open('/home/deepu/Dropbox/I-Extractor/I-Extractor.pkl','rb') as modelFile:      #importing pickle model
    model = pickle.load(modelFile)

    
filename = ""
app=Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')                                              
if not os.path.isdir(UPLOAD_FOLDER):                             #creating uploads folder 
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
        image_to_text = []
        result = ""
        if 'file' not in request.files:             # check if the post request has the file part
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
            dst = cv2.fastNlMeansDenoisingColored(img ,None, 10, 10, 7, 15)      #removing noise from the image
            image_to_text.append(pytesseract.image_to_string(dst, lang='eng+hin'))
            prediction = model(image_to_text[0])
            for ent in prediction.ents:                                          # predicting entities
                result = result + '\n' + ent.label_ + ":" + ent.text
            return result
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
        
if __name__ == "__main__":
    app.run(host = '127.0.0.1',port = 5005, debug = False)      #running application server
