import numpy as np
import pandas as pd

import os
import random
from operator import itemgetter
import copy
import time

import torch
import torchvision
import torchvision.transforms as transform
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, Dataset, ConcatDataset
import torch.nn as nn
import torchvision.models as models
from torchvision.utils import make_grid
import torch.nn.functional as F

#from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix, classification_report

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import imread
#import seaborn as sns

from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt # for plotting
import numpy as np # for transformation

import torch # PyTorch package
import torchvision # load datasets
import torchvision.transforms as transforms # transform data
import torch.nn as nn # basic building block for neural neteorks
import torch.nn.functional as F # import convolution functions like Relu
import torch.optim as optim # optimzer

device= torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

def return_prediction(filename = 'densenet121_0cpu.pth', img='img_0467_720.jpg' ):
    # client = storage.Client()
    # bucket = storage_client.bucket(bucket_name)
    # blob = bucket.blob(blob_name)
    # blob.download_to_filename(filename)
    pretrained_model = models.densenet121(weights=True)
    num_features = pretrained_model.classifier.in_features
    # Define a new classifier with 6 output units
    new_classifier = nn.Linear(num_features, 6)
    pretrained_model.classifier = new_classifier
    device = torch.device('cpu')
    pretrained_model.load_state_dict(torch.load(filename, map_location=device))
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
