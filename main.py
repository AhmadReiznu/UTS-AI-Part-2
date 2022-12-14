# Reiznu Ahmad Tjandrida
# 21091397018

# UTS AI ke 2

# Mengimport Library numpy, dan memberi inisial
import numpy as np

# Layer input 10 featurese
inputs = [
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.9, 4.5, 5.0, 5.5],
    [1.5, 1.4, 2.2, 2.4, 3.2, 3.4, 4.2, 4.4, 5.2, 5.4],
    [3.5, 18.5, 18.0, 20.5, 30.0, 30.5, 40.0, 40.5, 50.0, 50.5],
    [2.7, 1.8, 2.6, 2.8, 3.6, 3.8, 4.6, 4.8, 5.6, 5.8],
    [2.5, 6.4, 7.2, 7.4, 8.2, 8.4, 9.2, 9.4, 10.2, 10.4],
    [12.5, 16.4, 17.2, 17.4, 18.2, 18.4, 19.2, 19.4, 10.2, 10.4],
]

weights_1 = [
    [1.0, 1.5, 2.0, 2.5, 3.7, 3.5, 4.7, 4.5, 5.0, 5.5],
    [1.5, 1.4, 2.2, 2.4, 3.2, 3.4, 4.2, 4.4, 5.2, 5.4],
    [2.7, 1.8, 2.6, 2.8, 3.6, 3.8, 4.6, 4.8, 5.6, 5.8],
    [2.5, 6.4, 7.2, 7.4, 8.2, 8.4, 9.2, 9.4, 10.2, 10.4],
    [3.5, 18.5, 18.0, 20.5, 30.0, 30.5, 40.0, 40.5, 50.0, 50.5]
]

biases_1 = [1.5, 2.3, 3.1, 4.7, 5.8]

weights_2 = [
    [0.2, 0.4, 0.6, 0.8, 1.0],
    [2.7, 1.8, 2.6, 2.8, 3.6],
    [1.0, 1.5, 2.0, 2.5, 3.7]
]
biases_2 = [1.9, 5.6, 4.3]

# np.array, membuat sebuah matriks dari array yang ada
outputs_1 = np.dot(inputs, np.array(weights_1) . T) + biases_1
outputs_2 = np.dot(outputs_1, np.array(weights_2) . T) + biases_2
print(outputs_2)
