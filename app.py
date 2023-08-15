from flask import Flask, request, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
import io
import base64

app = Flask(__name__)
model = tf.keras.models.load_model('arun')

@app.route('/', methods=['GET', 'POST'])
def upload():
    result_display = False 
    predict = ""  
    img_data = None 

    if request.method == 'POST':
        file = request.files['image']
        if file:
            img = Image.open(file.stream).convert('RGB')
            img = img.resize((100, 100))

            img_array = np.array(img)
            img_array = img_array / 255.0

            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            class_index = np.argmax(prediction)
            result_display = True

            if class_index == 1:
                predict = 'The person has pneumonia he has to consult doctor'
            else:
                predict = 'The person is normal'

            img_byte_array = io.BytesIO()
            img.save(img_byte_array, format='PNG')
            img_data = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    return render_template('index.html', result_display=result_display, predict=predict, img_data=img_data) 

if __name__ == "__main__":
    app.run(debug=True)
