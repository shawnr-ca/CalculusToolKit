import matplotlib.pyplot as plt
import numpy as np


X = np.linspace(-10, 10, 1000)

y = np.e**(np.sin(X))
def func(x):
    return np.e**(np.sin(x))

func_int = 25.0755011589


inter = [-10,10]


inter_dist = (inter[1]-inter[0])




accu_list = []
rect_num_iters = 200
for rects in range(1,rect_num_iters):
    rect_areas = []
    rect_width = inter_dist / rects
    for rect in range(rects):
        rect_areas.append(rect_width*func(inter[0] + rect*rect_width))
    integral_approx = sum(rect_areas)
    print(integral_approx)
    accu_list.append(100*integral_approx/func_int)


def plot():
    fig, ax = plt.subplots()
    ax.plot(accu_list)
    plt.ylabel("Percent Accuracy of Rectanguler Integration")
    plt.xlabel("Number of Rectangles")
    plt.title("Rectangular vs Definite Integration of f(x) = e^sin(x)")
    plt.show()



plot()