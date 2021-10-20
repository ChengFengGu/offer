#!/usr/bin/env python
# coding: utf-8

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import xgboost as xgb
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split

x1 = np.arange(0, 100, 1)
a = 0.3 * x1 + 1
b = 0.3 * x1 - 1
x2 = np.concatenate((a[0:50], b[50:]), axis=0)


data = []
idx = 0
for a_t, b_t in zip(x1.tolist(), x2.tolist()):
    if idx < 50:
        data.append((a_t, b_t, 0))
    else:
        data.append((a_t, b_t, 1))
    idx += 1
data = pd.DataFrame(data, columns=["x1", "x2", "label"])


sns.scatterplot(data["x1"], data["x2"], hue=data["label"])
plt.savefig("ROC曲线.png")


x_train = data[["x1", "x2"]].values
y_train = data["label"].values.astype("int")

x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.3)


dtrain = xgb.DMatrix(x_train, label=y_train)
dtest = xgb.DMatrix(x_test, label=y_test)

param = {"max_depth": 2, "eta": 1, "objective": "binary:logistic"}  # 设置XGB的参数，使用字典形式传入
num_round = 2  # 使用线程数
bst = xgb.train(param, dtrain, num_round)  # 训练
preds = bst.predict(dtest)  # 预测
# preds = np.array([1 if e>0.5 else 0 for e in preds])
# accuracy_score(preds,y_test)


roc_auc_score(y_test, preds)

fpr, tpr, thresholds = roc_curve(y_test, preds, pos_label=1)

thresholds
