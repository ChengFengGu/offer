import torch 
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self,in_feats:int):
        # self.conv = nn.Conv2d(28,56,kernel_size=3)
        
        self.layers = nn.Sequential(
            nn.Conv2D(in_feats,256,3),
            nn.ReLU(),
            nn.Conv2d(256,512,3),
            nn.ReLU(),
            nn.MaxPool(),
            nn.Conv2D(512,512,3),
            nn.ReLU(),
            nn.AvgPool()        
        )

        self.cls = nn.Sequential(
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Softmax(dim=2)
        )

    def forward(self,x):
        x_feat = self.layers(x)
        x_flatten = x.flatten()
        pred = self.cls(x_flatten)
        return pred

if __name__ == "__main__":
    a = torch.rand(3,28,28)
    model = Model()
    pred = model(a)