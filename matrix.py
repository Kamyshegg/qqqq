import numpy as np 
qwerty=np.load('qwert_1.npz')
matrix1=(qwerty['arr_0'])
matrix2=(qwerty['arr_1'])
qw=np.dot(matrix1, matrix2)
print(qw)