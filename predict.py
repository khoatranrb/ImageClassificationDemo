import numpy as np

from keras.models import load_model, model_from_json, clone_model
import tensorflow as tf

def predict(InputModel_image, model, labelNames):

	predicts = model.predict(InputModel_image)
	predictLabel = labelNames[np.argmax(predicts)]

	return predictLabel
