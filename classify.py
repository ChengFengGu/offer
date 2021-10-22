import torch 

import torch.nn as nn

import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self,):
        self.conv = nn.Conv2d(28,56,kernel_size=3)
        
        self.layers = nn.Sequential(
            nn.Conv2D(28,256,3)
            nn.ReLu()
            nn.Conv2d(256,512,3)
            nn.ReLu()
            nn.MaxPool()
            nn.Conv2D()
            
        )