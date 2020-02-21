import cv2
from base64 import decodestring
import numpy as np

def decode_content(content):
    # content is a base64 jpeg
    data = decodestring(content.encode('ascii'))
    return data

def convert_jpeg_to_numpy(jpeg):
    # jpeg is raw data (in jpeg format)
    image = cv2.imdecode(np.fromstring(jpeg, dtype=np.uint8), -1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def prepare_model_input(image):
    InputModel_image = cv2.resize(image, (32, 32))
    InputModel_image = np.expand_dims(InputModel_image.astype("float") / 255.0, axis=0)
    return InputModel_image

def process_image(contents):
    image = contents.split(',')[1]
    data = decode_content(image)

    image = convert_jpeg_to_numpy(data)
    return image