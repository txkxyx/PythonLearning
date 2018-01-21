import numpy as np

# ANDゲート
def AND_no(x1,x2):
    w1, w2, theta = 0.5 ,0.5 ,0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1 

#print(AND_no(0.9,0.9))

# バイアスANDゲート
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([1,1])
    b = 0
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#print(AND(0.3,0.4))

# NANDゲート
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-1,-1])
    b = 0
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# ORゲート
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([1,1])
    b = 0
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# XORゲート
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))