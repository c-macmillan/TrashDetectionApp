
import torch
import torch.nn as nn
import torchvision.models as models

# import warnings
# warnings.filterwarnings('ignore')

import torch # PyTorch package
import torchvision.transforms as transforms # transform data
import torch.nn as nn # basic building block for neural networks
from io import BytesIO
import sys

device= torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
pretrained_model = torch.jit.load('model_scripted.pt')

def return_prediction(filename = 'model_scripted.pt', img='img_0467_720.jpg' ):
    print("Starting Predictions\n\n")
    transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((224,224)),
    transforms.Normalize((0.485, 0.456, 0.406),(0.229,0.224,0.225)),
    transforms.CenterCrop(255),
    ])
    print('pre transform', file=sys.stderr)
    img = transform(img)
    print('post transform', file=sys.stderr)
    img = torch.unsqueeze(img, 0)  # Add a batch dimension to the image tensor
    pretrained_model.eval()
    with torch.no_grad():
        output = pretrained_model(img)
        probabilities = torch.nn.functional.softmax(output, dim=1)
        predicted_class_idx = torch.argmax(probabilities, dim=1)
    return predicted_class_idx.item(), torch.max(probabilities).data.numpy()
