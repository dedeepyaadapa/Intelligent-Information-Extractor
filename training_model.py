from trainingdata import TRAIN_DATA
from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm
import pickle

model = None
output_dir=Path("/home/deepu/Dropbox/I-Extractor/MODEL")
n_iter=100


if model is not None:         #creating blank model
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  
    print("Created blank 'en' model")


    
if 'ner' not in nlp.pipe_names:      #setting up the pipeline
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)
else:
    ner = nlp.get_pipe('ner')

    

for _, annotations in TRAIN_DATA:       # adding labels to the model
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])


        
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']         #training the model
with nlp.disable_pipes(*other_pipes):  
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in tqdm(TRAIN_DATA):
            nlp.update(
                [text],  
                [annotations],  
                drop=0.5,  
                sgd=optimizer,
                losses=losses)
        print(losses)




if output_dir is not None:       #saving the model
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    model=output_dir
    print("Saved model to", output_dir)

    
    
with open('/home/deepu/Dropbox/I-Extractor/I-Extractor_Model.pkl','wb') as modelFile:  #generating pickle file
     pickle.dump(nlp,modelFile)





