import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.datasets import FashionMNIST

import numpy as np 


def input_transform():
    transforms.Compose([transforms.Normalize(), transforms.ToTensor()])

def set_seed():
    torch.random.seed(2021)
    np.random.seed(2021)


class Model(nn.Module):
    def __init__(self, in_feats: int, cls_num: int = 2):
        # self.conv = nn.Conv2d(28,56,kernel_size=3)
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(in_feats, 256, 3),
            nn.ReLU(),
            nn.Conv2d(256, 512, 3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3),
            # nn.BatchNorm2d(),
            nn.Conv2d(512, 512, 3),
            nn.ReLU(),
            nn.AvgPool2d(kernel_size=3),
        )

        self.cls = nn.Sequential(
            nn.Linear(2048, 1024),
            nn.ReLU(),
            nn.Linear(1024, 256),
            nn.ReLU(),
            nn.Linear(256, cls_num),
            nn.ReLU(),
        )

    def forward(self, x: torch.Tensor):
        N, C, H, W = x.shape
        x_feat = self.layers(x)
        # x_flatten = x_feat.flatten()
        x_flatten = x_feat.view(N, -1)
        pred = self.cls(x_flatten)
        result = F.softmax(pred)

        return result


def get_set_loader():
    fashion_mnist_train = FashionMNIST(
        download=True, root="转转/torch分类/fashion_mnist", train=True
    )
    fashion_mnist_test = FashionMNIST(
        download=True, root="转转/torch分类/fashion_mnist", train=False
    )
    train_dataloader = DataLoader(fashion_mnist_train, batch_size=32, shuffle=True)
    test_dataloader = DataLoader(fashion_mnist_test, batch_size=32, shuffle=False)


def train():pass

if __name__ == "__main__":
    a = torch.rand(12, 3, 28, 28)
    model = Model(in_feats=3)
    pred = model(a)

    labels = [torch.argmax(pred[i]) for i in range(len(pred))]
    print(labels)
