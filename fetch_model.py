from google.cloud import storage
import torch
import torchvision
import torchvision.transforms as transform
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, Dataset, ConcatDataset
import torch.nn as nn
import torchvision.models as models
from torchvision.utils import make_grid
import torch.nn.functional as F
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import imread
import torchvision.transforms as transforms

from img_file import img #retrieves the img uploaded by user


#bucket = storage_client.bucket("trashclassifierapp")
#blob = bucket.blob("densenet121_0cpu.pth")
#blob.download_to_filename('dense_blob.pth')

# Load the pre-trained model
#pretrained_model = models.densenet121(weights=True)

# Get the number of input features in the last classifier layer
#num_features = pretrained_model.classifier.in_features

# Define a new classifier with 6 output units
#new_classifier = nn.Linear(num_features, 6)

# Replace the last classifier layer in the pre-trained model
#pretrained_model.classifier = new_classifier

#device = torch.device('cpu')

#pretrained_model.load_state_dict(torch.load('dense_blob.pth', map_location=device))

'''
Functions fetches a model from gcs bucket and predicts class of img.
Not importing img on file yet.
'''

def return_prediction(bucket_name, blob_name, filename, img):
    client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(filename)
    pretrained_model = models.densenet121(weights=True)
    num_features = pretrained_model.classifier.in_features
    # Define a new classifier with 6 output units
    new_classifier = nn.Linear(num_features, 6)
    pretrained_model.classifier = new_classifier
    device = torch.device('cpu')
    pretrained_model.load_state_dict(torch.load('dense_blob.pth', map_location=device))
    img = mpimg.imread(img)
    transform = transforms.Compose([
     transforms.ToTensor(),
    transforms.Resize((224,224)),
    transforms.Normalize((0.485, 0.456, 0.406),(0.229,0.224,0.225)),
    transforms.CenterCrop(255),
    ])
    img = transform(img)
    img = torch.unsqueeze(img, 0)  # Add a batch dimension to the image tensor
    pretrained_model.eval()
    with torch.no_grad():
    output = pretrained_model(img)
    probabilities = torch.nn.functional.softmax(output, dim=1)
    predicted_class_idx = torch.argmax(probabilities, dim=1)
    return predicted_class_idx.item()

# Print the predicted class index and corresponding probability
#print('Predicted class index:', predicted_class_idx.item())
#print('Predicted class probability:', probabilities[0, predicted_class_idx].item())
    
    
    
    
