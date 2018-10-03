'''
Using monte carlo method estimate the value of pi
generate a large number of random points and see how many fall in the circle enclosed by the unit square.
REF: pi_op for visualization
'''

import numpy as np
import matplotlib.pyplot as plt


box_area = 4.0

N_total = 1000000

X = np.random.uniform(low=-1 , high=1 , size=N_total)
Y = np.random.uniform(low=-1 , high=1 , size=N_total)

distance = np.sqrt(X**2+Y**2)

is_pt_inside = distance<1.0

N_inside=np.sum(is_pt_inside)

circle_area = box_area * N_inside/N_total

plt.scatter(X[0:1000],Y[0:1000],  s=40,c=is_pt_inside[0:1000],alpha=.6, edgecolors='None')  
plt.axis('equal')

print("Area of circle = ", circle_area)
print("pi = ",np.pi)
plt.show()
