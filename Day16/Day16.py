import numpy as np
import matplotlib.pyplot as plt

# compute the x and y coor for points on a sine curve:
# np.arange(): NumPy 中用于创建等间距数值数组的函数， 类似于python中的range
# np.arange(start, stop, step)
x = np.arange(0, 3 * np.pi, 0.1)   
y_sine = np.sin(x)
y_cosine = np.cos(x)

# Plot the points using matplotlib:
plt.plot(x, y_sine, label = "sine wave")
plt.plot(x, y_cosine, label = "cosine wave")

#create labels:
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("Sine and Cosine")
plt.legend()

plt.show()      # must call plt.show() to make graphics appear


# 需要先用 plt.plot() 画好线，并设置好 label，然后再调用 plt.legend()，这样图例才能正确显示。
# 如果你在 plt.plot() 之前就写 plt.legend()，图例会是空的或不完整。
# 一般顺序如下：
# plt.plot(..., label=...) 画线并加标签
# plt.xlabel()、plt.ylabel()、plt.title() 设置标签和标题
# plt.legend() 显示图例
# plt.show() 显示图形







