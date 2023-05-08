import matplotlib.pyplot as plt
import numpy as np
import math

x = range(1, 5000)
# Functions represented as polynomial P(i) such that i = O(n)
y = [(i**3) for i in x]
y1 = [(i**3)/2 for i in x]

plt.plot(x, y)
plt.plot(x, y1)
plt.legend(['NormalRSA Encryption O(n^3)', 'EnhancedRSA Encryption O(n^3/2) e < sqrt(Φ(n))'])
plt.title('Encrytion Time complexity')
plt.ylabel('Time')
plt.xlabel('n-bits size')
plt.show()