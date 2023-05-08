import matplotlib.pyplot as plt
import numpy as np
import math

x = range(1, 5000)
# Functions represented as polynomial P(i) such that i = O(n)
y = [(i**3) for i in x]
y1 = [2*((i/2)**3) for i in x]

plt.plot(x, y)
plt.plot(x, y1)
plt.legend(['NormalRSA Decryption O(n^3)', 'EnhancedRSA Decryption 2O((n/2)^3) CRT'])
plt.title('Decrytion Time complexity')
plt.ylabel('Time')
plt.xlabel('n-bits size')
plt.show()