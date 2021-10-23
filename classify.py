import torch 
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self,in_feats:int):
        # self.conv = nn.Conv2d(28,56,kernel_size=3)
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(in_feats,256,3),
            nn.ReLU(),
            nn.Conv2d(256,512,3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3),
            nn.Conv2d(512,512,3),
            nn.ReLU(),
            nn.AvgPool2d(kernel_size=3)        
        )

        self.cls = nn.Sequential(
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Softmax(dim=2)
        )

    def forward(self,x:torch.Tensor):
        x_feat = self.layers(x)
        x_flatten = x_feat.flatten()
        pred = self.cls(x_flatten)
        return pred

if __name__ == "__main__":
    a = torch.rand(3,28,28)
    model = Model(in_feats=3)
    pred = model(a)