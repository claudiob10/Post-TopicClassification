 
import json
import numpy as np
import os
import pickle
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
 
from azureml.core.model import Model
 
def init():
    global topicclassifier,vectorizer
    # retrieve the path to the model file using the model name
    model_path1 = Model.get_model_path('vectorizer')
    model_path2 = Model.get_model_path('topicclassifier')
    vectorizer = joblib.load(model_path1)
    topicclassifier = joblib.load(model_path2)
 
def run(raw_data):
    data =  np.array(json.loads(raw_data)['data'])
    # make prediction
    y_hat = topicclassifier.predict(vectorizer.transform(data))
    return json.dumps(y_hat.tolist())
