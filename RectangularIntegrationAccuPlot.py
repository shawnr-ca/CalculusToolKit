import matplotlib.pyplot as plt
import numpy as np


X = np.linspace(-10, 10, 1000)

y = 16 - X**2
def func(x):
    return 16 - x**2

func_int = 256/3


inter = [-4,4]


inter_dist = (inter[1]-inter[0])




accu_list = []
rect_num_iters = 1000
for rects in range(1,rect_num_iters):
    rect_areas = []
    rect_width = inter_dist / rects
    for rect in range(rects):
        rect_areas.append(rect_width*func(inter[0] + rect*rect_width))
    integral_approx = sum(rect_areas)
    print(integral_approx)
    accu_list.append(integral_approx/func_int)


def plot():
    fig, ax = plt.subplots()
    ax.plot(accu_list)
    plt.ylabel("Accuracy of Rectanguler Integration")
    plt.xlabel("Number of Rectangles")
    plt.title("Rectangular vs Definite Integration of f(x) = 16 - x^2")
    plt.show()

def plot1():
    fig, ax = plt.subplots()
    ax.plot(accu_list[100:])
    plt.ylabel("Accuracy of Rectanguler Integration")
    plt.xlabel("Number of Rectangles")
    plt.title("Rectangular vs Definite Integration of f(x) = 16 - x^2")
    plt.show()

plot()