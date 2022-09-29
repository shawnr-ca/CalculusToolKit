import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

user_x1 = float(input("What is the lower bound of the interval for the Riemman Sum you would like to calculate?"))
user_x2 = float(input("What is the upper bound of the interval for the Riemman Sum you would like to calculate?"))
user_num_rect = int(input("How many rectangles would you like to approximate with?"))

inter = [user_x1,user_x2]
X = np.linspace(int(inter[0]*1.1), int(inter[1]*1.1), 1000)

y = np.e**(np.sin(X))
def func(x):
    return np.e**(np.sin(x))

func_int = 9.892537052

rect_num = user_num_rect


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
plt.show()
