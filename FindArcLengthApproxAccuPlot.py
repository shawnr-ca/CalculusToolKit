import matplotlib.pyplot as plt
import numpy as np


X = np.linspace(-10, 10, 1000)

y = np.e**(np.sin(X))
def func(x):
    return np.e**(np.sin(x))

def FindSegDist(x1,x2):
    dist = np.sqrt((x2-x1)**2 + ((func(x2)-func(x1)))**2)
    return dist

func_length = 26.353723925


inter = [-10,10]


inter_dist = (inter[1]-inter[0])


x1 = inter[0]
x2 = inter[1]
inter_len = (x2-x1)

accu_list = []
lin_num_iters = 100
lin_seg_len = 0
for i in range(1,lin_num_iters):
    lin_seg_x = inter_len / i
    lin_seg_len = 0
    x1 = inter[0]
    x2 = inter[1]
    while x1 < x2:
        lin_seg_len += FindSegDist(x1, (x1 + lin_seg_x))
        x1 += lin_seg_x
    if round(x1,10) <= x2:
        accu_list.append(100*lin_seg_len/func_length)
    else:
        accu_list.append(100*(lin_seg_len-FindSegDist(x1-lin_seg_x, (x1)))/func_length)
    print(lin_seg_len)


def plot():
    fig, ax = plt.subplots()
    ax.plot(accu_list)
    plt.ylabel("% Accuracy of Function Arc Length Approximation")
    plt.xlabel("Number of Line Segments")
    plt.title("Formulaic Calculation vs Algorithmic Approximation of Function's Arc Length")
    plt.show()

plot()