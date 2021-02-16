import pytesseract
import os
import spacy
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix
import pandas as pd



image_to_text=[]           #extracting text from pancards
directory = '/home/deepu/Dropbox/I-Extractor/pancards-testing'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_to_text.append(pytesseract.image_to_string(os.path.join(directory, filename), lang='eng+hin'))


        
        
pred1=[]       #Testing the model
pred2=[]
for text  in image_to_text:
    nlp2 = spacy.load('/home/deepu/Dropbox/I-Extractor/MODEL')
    doc2 = nlp2(text)
    i=0
    for ent in doc2.ents:
        pred1.append(ent.text) 
    pred2.append(pred1)
    pred1=[]
pred3=[]
for i in pred2:
    if i==[]:
        pass
    else:
        pred3.append(i)
        
        
        
        

df = pd.DataFrame(pred3,columns =['ACCHOLDER','FATHER NAME','DOB','ACCNO'])  #saving predictions into csv file
df.to_csv('/home/deepu/Dropbox/I-Extractor/pred.csv', index=False)




df1=pd.read_csv('/home/deepu/Dropbox/I-Extractor/ACTUAL.csv')  #finding accuracy of model
df2=pd.read_csv('/home/deepu/Dropbox/I-Extractor/pred.csv')
x1=confusion_matrix(df1['ACCHOLDER'],df2['ACCHOLDER'])
x2=confusion_matrix(df1['FATHER NAME'],df2['FATHER NAME'])
x3=confusion_matrix(df1['DOB'],df2['DOB'])
x4=confusion_matrix(df1['ACCNO'],df2['ACCNO'])
y1=np.trace(x1)
y2=np.trace(x2)
y3=np.trace(x3)
y4=np.trace(x4)
z1=np.sum(x1)
z2=np.sum(x2)
z3=np.sum(x3)
z4=np.sum(x4)
Accuracy=(y1+y2+y3+y4)/(z1+z2+z3+z4)
print(Accuracy)




