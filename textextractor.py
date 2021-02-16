from PIL import Image
import pytesseract
import os



def img_to_str():           #extracting text from PAN cards
    image_to_text=[]
    directory = '/home/deepu/Dropbox/I-Extractor/pancards-training'
    for filename in os.listdir(directory):
        path=os.path.join(directory,filename)
        for filenames in os.listdir(path):
            if filenames.endswith(".jpg") or filenames.endswith(".png") or filenames.endswith(".jpeg"):
                image_to_text.append(pytesseract.image_to_string(os.path.join(path, filenames), lang='eng+hin'))
    return image_to_text

