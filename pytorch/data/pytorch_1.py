# -*- coding: UTF-8 -*-
from __future__ import print_function
import torch.optim as optim
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import os
import torch as t
import torch.nn as nn
import torch.nn.functional as F

t.__version__

x1 = t.Tensor(5, 3)
x2 = t.Tensor([[1, 2], [3, 4]])
print(x2)
x3 = t.rand(5, 3)
print(x3)
print("tensor-->", x3.size(0))
a = t.ones(3)
print(a)

c = t.rand(5, 1)
print(c)
s = c[3].item()
print(s)
cc = t.Tensor([[1, 2], [0, 1], [2, 3], [4, 5]])
dd = cc.detach()
dd.add_(2)

xx = t.ones(3, 3, requires_grad=True)
print(xx)
y = xx.sum()
print("tensor.sum-->", y)
print(y.grad_fn)

a = t.arange(0, 6)
print("tensor-->arange", a)
b = a.view(-1, 3)
print(b)

bb = t.ones([2, 3])
print(bb.sum(dim=0, keepdims=False))

print("--------------比较-----------")
a = t.linspace(0, 15, 6).view(2, 3)
b = t.linspace(15, 0, 6).view(2, 3)
print("a>b", a < b)
print("a[a>b]-->", a[a > b])
print("a.max(a,dim=0)-->", t.max(a, dim=0))
