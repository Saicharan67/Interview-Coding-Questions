import numpy as np

n, m = map(int, input().split())

X = []  # initialising X

Y = []  # initialising Y

for i in range(n):
    temp = list(map(int, input().split()))
    X.append(temp)

temp2 = list(map(int, input().split()))
for i in range(m):
    Y.append([temp2[i]])

X = np.array(X)     # converting to Numpy array
Y = np.array(Y)     # converting to Numpy array

x_transpose = np.transpose(X)               # calculating transpose
x_transpose_dot_x = x_transpose.dot(X)      # calculating dot product
temp_1 = np.linalg.inv(x_transpose_dot_x)   # calculating inverse


temp_2 = x_transpose.dot(Y)

Ɵ = temp_1.dot(temp_2)
