import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

X = np.linspace(-10, 10, 1000)

y = np.e**(np.sin(X))
def func(x):
    return np.e**(np.sin(x))

func_int = 9.892537052

rect_num = 30
inter = [-4,4]


inter_dist = (inter[1]-inter[0])
rect_width = inter_dist/rect_num

rect_areas = []

fig, ax = plt.subplots()
ax.plot(X,y)

for rect in range(rect_num):
    rect_areas.append(rect_width*func(inter[0] + rect*rect_width))
    ax.add_patch(Rectangle(((inter[0] + rect*rect_width), 0), rect_width, func(inter[0] + (rect+1)*rect_width)))


integral_approx = sum(rect_areas)
print(integral_approx)
plt.text(-8,15,"Rectangular Integration Result: " + str(integral_approx))
plt.text(-8,10,"Integral: " + str(func_int))
plt.show()