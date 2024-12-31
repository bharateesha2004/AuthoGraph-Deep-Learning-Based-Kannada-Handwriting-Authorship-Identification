import os
from flask import Flask, request, render_template, redirect, url_for
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Suppress TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('ERROR')

# Load the trained model
model_path = r'C:\Users\Dragon\Desktop\author detectio_package\authorship_detection_model.h5'
model = tf.keras.models.load_model(model_path)

# Function to preprocess the input image
def preprocess_image(img_path, target_size=(150, 150)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Function to predict the author
def predict_author(img_path):
    img_array = preprocess_image(img_path)
    predictions = model(img_array, training=False).numpy()
    predicted_class = np.argmax(predictions) + 1  # Adjust class labels by adding 1
    predicted_prob = np.max(predictions)
    
    # If one class has a probability above 99.5%
    if predicted_prob >= 0.995:
        return f"The predicted author is {predicted_class}."
    else:
        result = f"The predicted author is {predicted_class}.\n"
        other_classes = np.argsort(predictions[0])[::-1][1:4] + 1  # Adjust other class labels by adding 1
        result += "It could be one of these as well:\n"
        for cls in other_classes:
            result += f"Class {cls}\n"
        return result

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            result = predict_author(filepath)
            return render_template('index.html', prediction=result)
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)