import matplotlib.pyplot as plt
import numpy as np
import math

x = range(1, 4000)
# Functions represented as polynomial P(i) such that i = O(n)
y = [2*(i**4) + 4*(i**3) + 2*(i**2) for i in x]
y1 = [(i**4) + (2.75 * (i**3)) + (i**1.58) + i for i in x]

plt.plot(x, y)
plt.plot(x, y1)
plt.legend(['Overall NormalRSA 2O(n^4) + 4O(n^3) + 2O(n^2)', 'Overall EnhancedRSA O(n^4) + (11/4)O(n^3) + O(n^1.58) + O(n)'])
plt.title('Overall Normal RSA versus Proposed RSA Time complexity')
plt.ylabel('Time')
plt.xlabel('n-bits size')
plt.show()