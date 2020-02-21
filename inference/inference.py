import numpy as np

from keras.models import load_model, model_from_json, clone_model
import tensorflow as tf
from keras import backend as K

def _load_model(filePath):
    return load_model(filePath)

def predict(InputModel_image, model):

    labelNames = ['airplane', 'automotobile', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    predicts = model.predict(InputModel_image)
    predictLabel = labelNames[np.argmax(predicts)]

    return predictLabel

def debug_mode_clear_session():
    K.clear_session()
