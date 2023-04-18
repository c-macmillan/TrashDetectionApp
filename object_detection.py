import numpy as np
from Object import Object

def detect_objects(image_data):
    # Simulate object detection by generating some dummy data
    labels = ['recycling', 'trash', 'compost']
    probabilities = np.random.uniform(0.5, 0.9, size=len(labels))
    xmins = np.random.uniform(0, 0.5, size=len(labels))
    ymins = np.random.uniform(0, 0.5, size=len(labels))
    xmaxs = np.random.uniform(0.5, 1, size=len(labels))
    ymaxs = np.random.uniform(0.5, 1, size=len(labels))
    educations = ['Make sure you clean off any leftover food waste first', 'You hate the planet', 'Fertilizer']
    
    # Create a list of Object instances
    objects = []
    for label, probability, xmin, ymin, xmax, ymax, education in zip(labels, probabilities, xmins, ymins, xmaxs, ymaxs, educations):
        obj = Object(label, probability, xmin, ymin, xmax, ymax, image_data, education)
        objects.append(obj)
    
    return objects
