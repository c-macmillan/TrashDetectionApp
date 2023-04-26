from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
import base64
from prediction import return_prediction
from Object import Object
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Get the uploaded file and convert it to a numpy array
        file = request.files['file']
        image = Image.open(file)
        
        # Call the object detection model
        pred_id, probability = return_prediction(img = image)
        object = Object(pred_id, probability)

        # Convert the image data to base64 and pass it to the template
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        image_data_uri = base64.b64encode(buffered.getvalue()).decode("ascii")
        
        # Render the results template with the detected objects
        return render_template('results.html', object=object, image_data_uri=image_data_uri)
    
    # Render the upload form
    return render_template('upload.html')



if __name__ == '__main__':
    app.run(debug=True)



