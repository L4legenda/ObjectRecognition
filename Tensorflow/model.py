import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

np.set_printoptions(suppress=True)

model = tensorflow.keras.models.load_model('../../Tensorflow/keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def recognition(img):
    image = Image.open("upload/" + img)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)

    answer = {
        "Телевизор" : round(float(prediction[0][0]), 2),
        "Серво" : round(float(prediction[0][1]), 2),
        "Стакан" : round(float(prediction[0][2]), 2),
        "Ждун" : round(float(prediction[0][3]), 2),
        "Очки" : round(float(prediction[0][4]), 2),
        "Кастрюля" : round(float(prediction[0][5]), 2),
        "Кошка" : round(float(prediction[0][6]), 2),
    }
    print(answer)
    return answer


