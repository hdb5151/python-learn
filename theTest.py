import unittest
import torch

x = torch.rand(5, 5, requires_grad=True)
print("x==", x)

y = torch.rand(5, 5, requires_grad=True)
print("y==", y)

# z = x.add(y)
z = torch.sum(x + y)
print("z==", z)

z.backward()
print("x.grad==", x.grad)
