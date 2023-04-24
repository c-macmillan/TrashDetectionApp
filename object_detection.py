import numpy as np
from Object import Object

def detect_object(image_data):
    # Simulate object detection by generating some dummy data
    labels = ['recycling', 'trash', 'compost']
    pred_label = np.random.choice(labels, 1)[0]
    probability = np.random.uniform(0,1)
    education = {'recycling':'Make sure you clean off any leftover food waste first',
                 'trash': 'You hate the planet',
                 'compost': 'Fertilizer'}
    
    # Create a list of Object instances
    object = Object(pred_label, probability, image_data, education=education[pred_label])
    
    return object
