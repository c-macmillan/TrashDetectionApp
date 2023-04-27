
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

def return_prediction(filename = 'densenet121_0cpu.pth', img='img_0467_720.jpg' ):
    print("Starting Predictions\n\n")
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
    with open(filename, 'rb') as f:
        buffer = BytesIO(f.read())
    state_dict = torch.load(buffer, map_location=device)
    pretrained_model.load_state_dict(state_dict)
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
