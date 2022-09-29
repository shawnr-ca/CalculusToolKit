import matplotlib.pyplot as plt
import numpy as np

user_x1 = float(input("What is the lower bound of the interval for the length of the arc you would like to calculate?"))
user_x2 = float(input("What is the upper bound of the interval for the length of the arc you would like to calculate?"))
user_num_rect = int(input("How many line segments would you like to use?"))

inter = [user_x1,user_x2]
num_line_seg = user_num_rect

X = np.linspace(int(inter[0]*1.1), int(inter[1]*1.1), 1000)
y = np.e**(np.sin(X))
def func(x):
    return np.e**(np.sin(x))

def FindSegDist(x1,x2):
    dist = np.sqrt((x2-x1)**2 + ((func(x2)-func(x1)))**2)
    return dist

inter_len = (inter[1]-inter[0])
lin_seg_len = 0
lin_seg_x = inter_len/num_line_seg

x1 = inter[0]
x2 = inter[1]

lin_seg_num = 1

fig, ax = plt.subplots()
ax.plot(X,y)
line_list = []
while x1 < x2:
    X1,Y1 = [x1,x1+lin_seg_x],[func(x1),func(x1+lin_seg_x)]
    plt.plot(X1,Y1)
    lin_seg_len += FindSegDist(x1, (x1 + lin_seg_x))
    print(f"Line Segment #{lin_seg_num}: interval-{round(x1,5), round(x1+lin_seg_x, 5)}  Net Length {round(lin_seg_len,5)}")
    x1 += lin_seg_x
    lin_seg_num += 1


if round(x1,10) <= x2:
    print("\n")
    print(f"The approximate length of the function's arc within the interval {str(inter)} is: {round(lin_seg_len, 8)}")
else:
    print("\n")
    print(f"The approximate length of the function's arc within the interval {str(inter)} is: {round(lin_seg_len-FindSegDist(x1-lin_seg_x, (x1)), 8)}")

plt.show()

