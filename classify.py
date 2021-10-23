import torch 
import torch.nn as nn
import torch.nn.functional as F

from torchvision import transforms

def input_transform():
    transforms.Compose(
        [
            transforms.Normalize(),
            transforms.ToTensor()
        ]
    )
    

class Model(nn.Module):
    def __init__(self,in_feats:int,cls_num:int = 2):
        # self.conv = nn.Conv2d(28,56,kernel_size=3)
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(in_feats,256,3),
            nn.ReLU(),
            nn.Conv2d(256,512,3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3),
            # nn.BatchNorm2d(),
            nn.Conv2d(512,512,3),
            nn.ReLU(),
            nn.AvgPool2d(kernel_size=3)        
        )

        self.cls = nn.Sequential(
            nn.Linear(2048,1024),
            nn.ReLU(),
            nn.Linear(1024,256),
            nn.ReLU(),
            nn.Linear(256,cls_num),
            nn.ReLU(),
        )

        self.softmax = F.softmax(dim=cls_num)

    def forward(self,x:torch.Tensor):
        N,C,H,W = x.shape
        x_feat = self.layers(x)
        # x_flatten = x_feat.flatten()
        x_flatten = x_feat.view(N,-1)
        pred = self.cls(x_flatten)
        result = self.softmax(pred)
        
        return result

if __name__ == "__main__":
    a = torch.rand(12,3,28,28)
    model = Model(in_feats=3)
    pred = model(a)