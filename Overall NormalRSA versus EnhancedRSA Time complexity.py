import matplotlib.pyplot as plt
import numpy as np
import math

x = range(1, 5000)
# Functions represented as polynomial P(i) such that i = O(n)
y = [2*(i**4) + 4*(i**3) + 2*(i**2) for i in x]
y1 = [(i**4) + 1.75*(i**3) + (i**2) + (i**1.5) + i for i in x]

plt.plot(x, y)
plt.plot(x, y1)
plt.legend(['NormalRSA 2O(n^4) + 4O(n^3) + 2O(n^2)', 'EnhancedRSA O(n^4) + 7/4 O(n^3) + O(n^2) + O(n^1.58) + O(n)'])
plt.xlabel('n-bits size')
plt.title('Overall NormalRSA versus EnhancedRSA Time complexity')
plt.ylabel('Time')
plt.show()