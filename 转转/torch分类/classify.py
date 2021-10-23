import logging
import os
import sys
import traceback
from os.path import join

import numpy as np
import torch
from torch import optim
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset, random_split
from torchvision import transforms
from torchvision.datasets import FashionMNIST
from tqdm import tqdm, trange

from torch.optim import SGD, Adam


# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DEVICE = "cpu"


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
        logits = self.cls(x_flatten)
        proab = F.softmax(logits)

        return logits, proab


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


def compute_accuracy(model: nn.Module, val_loader: DataLoader):
    model = model.eval()
    logging.info("==> testing ...")
    all_num = 0
    acc_num = 0
    for batch_num, (feat, target) in enumerate(val_loader):
        feat = feat.to(DEVICE)
        target = target.to(DEVICE)
        logits, proab = model(feat)
        _, pred_labels = torch.max(proab, 1)
        all_num += target.size(0)
        acc_num += (pred_labels == target).sum()
    return acc_num * 1.0 / all_num * 1.0


def train(model: nn.Module, epochs: int = 20):
    # device = "cuda" if torch.cuda.is_available() else "cpu" 本机只支持CPU
    device = "cpu"
    # model = model.to(device)
    optimizer = SGD(model.parameters(), momentum=0.9)
    model = Model(in_feats=1, cls_num=10)
    train_loader, val_loader, test_loader = get_set_loader()

    for epoch in epochs:
        model = model.train()
        for batch_num, (feat, target) in enumerate(train_loader):
            feat = feat.to(device)
            target = target.to(device)

            logits, proab = model(feat)
            cost = F.cross_entropy(logits, target)  # 多分类交叉熵损失比较合适

            optimizer.zero_grad()
            cost.backward()
            optimizer.step()

            if batch_num % 50 == 0:
                logging.info(f"Epoch:{epoch} | batch:{batch_num} | cost:{cost}")
        accuracy = compute_accuracy(model, val_loader=val_loader)
        logging.info(f"Epoch {epoch} | accuracy:{accuracy:.2f}")

    logging.info("==> Final Testing ....")
    accuracy = compute_accuracy(model, test_loader)
    logging.info(f"Final Acc : {accuracy}")


if __name__ == "__main__":
    # a = torch.rand(12, 1, 28, 28)
    model = Model(in_chans=1, cls_num=10)
    model = model.to(DEVICE)
    
