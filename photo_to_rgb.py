import numpy as np
from PIL import Image

def create_image_array(file_name):
    '''
    Description: 
    Processes a JPG file by using the Image function from
    the Python Imaging Library (PIL) and converts it into
    a NumPy array. Extracts and returns the raw RGB pixel
    data from the new array. 

    Parameter:
    'file_name' = file path of the JPG file

    Returns:
    'raw_rgb' = NumPy array containing raw RGB pixel data
    for the image provided in the 'file_name' parameter.
    '''
    image = Image.open(file_name)   # Open the image file
    image_array = np.array(image)   # Convert to NumPy array
    raw_rgb = image_arr[:,:,:3]     # Extract the raw RGB data 
    return raw_rgb

def create_image(raw_rgb):
    '''
    Description: 
    Using the raw RGB data that is output from the 
    create_image_array function above and the
    Image.fromarray function in the Python Imaging Library
    (PIL), this function recreates the color image of
    the data provided.

    It also ensures that the data being recreated is of
    dtype = 'uint8', which is the standard data type for 
    RGB image data.

    Parameter:
    'raw_rgb' = NumPy array containing raw RGB pixel data.
    Output from the create_image_array function. 

    Returns:
    A PIL.Image.Image object. Shows the image in a notebook.
    '''
    raw_rgb_uint8 = np.array(raw_rgb, dtype='uint8')   # Ensures the NumPy array is of dtype 'uint8'
    return Image.fromarray(raw_rgb_uint8, 'RGB')       # Returns the image object