import logging
import os
import sys
import traceback
from os.path import join

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset, random_split
from torchvision import transforms
from torchvision.datasets import FashionMNIST
from tqdm import tqdm, trange


def setup_logging(
    output_folder, console="debug", info_filename="info.log", debug_filename="debug.log"
):
    """Set up logging files and console output.
    Creates one file for INFO logs and one for DEBUG logs.
    Args:
        output_folder (str): creates the folder where to save the files.
        debug (str):
            if == "debug" prints on console debug messages and higher
            if == "info"  prints on console info messages and higher
            if == None does not use console (useful when a logger has already been set)
        info_filename (str): the name of the info file. if None, don't create info file
        debug_filename (str): the name of the debug file. if None, don't create debug file
    """
    if os.path.exists(output_folder):
        raise FileExistsError(f"{output_folder} already exists!")
    os.makedirs(output_folder, exist_ok=True)
    # logging.Logger.manager.loggerDict.keys() to check which loggers are in use
    base_formatter = logging.Formatter("%(asctime)s   %(message)s", "%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    if info_filename != None:
        info_file_handler = logging.FileHandler(join(output_folder, info_filename))
        info_file_handler.setLevel(logging.INFO)
        info_file_handler.setFormatter(base_formatter)
        logger.addHandler(info_file_handler)

    if debug_filename != None:
        debug_file_handler = logging.FileHandler(join(output_folder, debug_filename))
        debug_file_handler.setLevel(logging.DEBUG)
        debug_file_handler.setFormatter(base_formatter)
        logger.addHandler(debug_file_handler)

    if console != None:
        console_handler = logging.StreamHandler()
        if console == "debug":
            console_handler.setLevel(logging.DEBUG)
        if console == "info":
            console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(base_formatter)
        logger.addHandler(console_handler)

    def exception_handler(type_, value, tb):
        logger.info("\n" + "".join(traceback.format_exception(type, value, tb)))

    sys.excepthook = exception_handler


def input_transform():
    transforms.Compose([transforms.Normalize(), transforms.ToTensor()])


def set_seed():
    torch.manual_seed(2021)
    np.random.seed(2021)


class Model(nn.Module):
    def __init__(self, in_chans: int, cls_num: int = 2):
        # self.conv = nn.Conv2d(28,56,kernel_size=3)
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(in_chans, 256, 3),
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

    train_size = int(0.8 * len(fashion_mnist_train))
    val_size = len(fashion_mnist_train) - train_size
    train_dataset, val_dataset = random_split(
        fashion_mnist_train, [train_size, val_size]
    )

    train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_dataloader = DataLoader(val_dataset, batch_size=32, shuffle=False)
    test_dataloader = DataLoader(fashion_mnist_test, batch_size=32, shuffle=False)

    return train_dataloader, val_dataloader, test_dataloader




def train(epochs:int = 20):
    model = Model(in_feats=1,cls_num=10)
    train_loader,val_loader,_ = get_set_loader()
    for epoch in epochs:
        for batch_num,(feat,label) in enumerate(train_loader):
            pass


if __name__ == "__main__":
    a = torch.rand(12,1,28,28)
    model = Model(in_chans=1,cls_num=10)
    result = model(a)
    print(result)
