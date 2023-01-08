import torch 
from PIL import Image
from torch import nn, save, load
from torch.optim import Adam
from torchvision.transforms import ToTensor
import numpy as np


class ImageClassifier(nn.Module): 
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(1, 32, (3,3)), 
            nn.ReLU(),
            nn.Conv2d(32, 64, (3,3)), 
            nn.ReLU(),
            nn.Conv2d(64, 64, (3,3)), 
            nn.ReLU(),
            nn.Flatten(), 
            nn.Linear(64*(28-6)*(28-6), 10)  
        )

    def forward(self, x): 
        return self.model(x)

# Instance of the neural network, loss, optimizer 
clf = ImageClassifier().to('cpu')
opt = Adam(clf.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss() 



def Classify(imgPath):
    

    with open('model_state.pt', 'rb') as f: 
        clf.load_state_dict(load(f))  

    img = Image.open(imgPath) 
    img_tensor = ToTensor()(img).unsqueeze(0).to('cpu')

    return (
        np.argmax(clf(img_tensor).detach().numpy()[0]),
        np.max(clf(img_tensor).detach().numpy()[0])
        )


if __name__ == "__main__": 
    print((Classify('img_3.jpg')))
    # Classify('img_2.jpg')
    # Classify('img_1.jpg')