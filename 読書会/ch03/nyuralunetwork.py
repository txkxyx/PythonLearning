
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype = np.int)

# x = np.arange(-5.0,5.0,0.1)
# y = step_function(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# x = np.arange(-5.0,5.0,0.1)
# y = sigmoid(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show() 

def relu(x):
    return np.maximum(0,x)

# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])
# print(np.dot(A,B))

X = np.array([1,2])
X.shape
W = np.array([[1,3,5],[2,4,6]])
print(W)
W.shape
Y = np.dot(X,W)
print(Y)

