import torch
import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

# prepare dataset


class DiabetesDataset(Dataset):
    def __init__(self, filepath):
        xy = np.loadtxt(filepath, delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]  # shape(多少行，多少列)
        self.x_data = torch.from_numpy(xy[:, :-1])  #加载所有行,加载除了最后一列外的 所有列数据
        self.y_data = torch.from_numpy(xy[:, [-1]])  #加载所有行,加载最后一列数据

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


dataset = DiabetesDataset('data/diabetes.csv')
train_loader = DataLoader(dataset=dataset,
                          batch_size=32,
                          shuffle=False,
                          num_workers=2)  #num_workers 多线程

# design model using class


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x


model = Model()

# construct loss and optimizer
criterion = torch.nn.BCELoss(reduction='mean')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# training cycle forward, backward, update
if __name__ == '__main__':
    for epoch in range(100):
        for i, data in enumerate(train_loader,
                                 0):  # train_loader 是先shuffle后mini_batch
            inputs, labels = data
            y_pred = model(inputs)
            loss = criterion(y_pred, labels)
            # print(epoch, i, loss.item())
            print(labels)
            optimizer.zero_grad()
            loss.backward()

            optimizer.step()

# import torch
# import numpy as np
# from torch.utils.data import Dataset
# from torch.utils.data import DataLoader
# from sklearn.model_selection import train_test_split

# # 读取原始数据，并划分训练集和测试集
# raw_data = np.loadtxt('data/diabetes.csv', delimiter=',', dtype=np.float32)
# X = raw_data[:, :-1]
# y = raw_data[:, [-1]]
# Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3)
# Xtest = torch.from_numpy(Xtest)
# Ytest = torch.from_numpy(Ytest)

# # 将训练数据集进行批量处理
# # prepare dataset

# class DiabetesDataset(Dataset):
#     def __init__(self, data, label):

#         self.len = data.shape[0]  # shape(多少行，多少列)
#         self.x_data = torch.from_numpy(data)
#         self.y_data = torch.from_numpy(label)

#     def __getitem__(self, index):
#         return self.x_data[index], self.y_data[index]

#     def __len__(self):
#         return self.len

# train_dataset = DiabetesDataset(Xtrain, Ytrain)
# train_loader = DataLoader(dataset=train_dataset,
#                           batch_size=32,
#                           shuffle=True,
#                           num_workers=1)  #num_workers 多线程

# # design model using class

# class Model(torch.nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()
#         self.linear1 = torch.nn.Linear(8, 6)
#         self.linear2 = torch.nn.Linear(6, 4)
#         self.linear3 = torch.nn.Linear(4, 2)
#         self.linear4 = torch.nn.Linear(2, 1)
#         self.sigmoid = torch.nn.Sigmoid()

#     def forward(self, x):
#         x = self.sigmoid(self.linear1(x))
#         x = self.sigmoid(self.linear2(x))
#         x = self.sigmoid(self.linear3(x))
#         x = self.sigmoid(self.linear4(x))
#         return x

# model = Model()

# # construct loss and optimizer
# criterion = torch.nn.BCELoss(reduction='mean')
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# # training cycle forward, backward, update

# def train(epoch):
#     train_loss = 0.0
#     count = 0
#     for i, data in enumerate(train_loader, 0):
#         inputs, labels = data
#         y_pred = model(inputs)

#         loss = criterion(y_pred, labels)

#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
#         train_loss += loss.item()
#         count = i

#     if epoch % 2000 == 1999:
#         print("train loss:", train_loss / count, end=',')

# def test():
#     with torch.no_grad():
#         y_pred = model(Xtest)
#         y_pred_label = torch.where(y_pred >= 0.5, torch.tensor([1.0]),
#                                    torch.tensor([0.0]))
#         acc = torch.eq(y_pred_label, Ytest).sum().item() / Ytest.size(0)
#         print("test acc:", acc)

# if __name__ == '__main__':
#     for epoch in range(50000):
#         train(epoch)
#         if epoch % 2000 == 1999:
#             test()