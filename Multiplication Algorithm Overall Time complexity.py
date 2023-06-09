import matplotlib.pyplot as plt
import numpy as np
import math

x = range(1, 10000)
# Functions represented as polynomial P(i) such that i = O(n)
y = [(i**2) for i in x]
y1 = [(i**1.58) for i in x]
y2 = [(i * (math.log(i))) for i in x]

plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)
plt.legend(['School Multiplication	O(n^2)','Karatsuba Multiplication	O(n^1.58)', 'Schonhage Strassen algorithm O(n log n)'])
plt.xlabel('n-bits size')
plt.title('Multiplication Algorithm Overall Time complexity')
plt.ylabel('Time')
plt.show()