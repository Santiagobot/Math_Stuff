# Hénon map

import numpy as np
import matplotlib.pyplot as plt

# Classical values for Henon Map
a = 1.5
b = 0.2

def Henon(x, y,):
    xn = 1  - (a) * x**2 + y
    yn = b * x

    return xn, yn

iteration = 10000

# Initial values

x0 , y0 = ((1-b)/2, (1-b)/2)

X, Y = [], []


for i in range(iteration):
    xn , yn = Henon(x0, y0)
    X, Y = X + [xn], Y + [yn]
    x0 , y0 = [xn, yn]

# Plot the graph

fig, ax = plt.subplots(figsize=(20,20))
ax.scatter(X, Y, color='green', s=0.5)
plt.show()


