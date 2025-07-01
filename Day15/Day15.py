import numpy as np

# a = np.array([1,2,3])
# print(type(a))
# print(a.shape)
# print(a[0], a[1], a[2])
# a[0] = 5
# print(a)

# b = np.array([[1,2,3],[4,5,6]])
# print(b.shape)
# print(b[0,0], b[0,1], b[1,0])

# Numpy also provides many functions to create arrays:
# a = np.zeros((3,2))
# print(a)
# b = np.ones((1,2))
# print(b)
# c = np.full((2,3), 7)
# print(c)
# d = np.eye(5)
# print(d)
# e = np.random.random((2,2)) # Create an array filled with random values
# print(e)

# Array indexing
# a = np.array([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])
# print(a)
# # Use slicing to pull out the subarray consisting of the first 2 rows
# # and columns 1 and 2; b is the following array of shape (2, 2):
# b = a[:2, 1:3]
# print(b)
# # A slice of an array is a view into the same data, so modifying it
# # will modify the original array.
# b[0,0] = 778899
# print(a)

# You can also mix integer indexing with slice indexing:
# a = np.array([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])
# print(a)
# # Two ways of accessing the data in the middle row of the array.
# # Mixing integer indexing with slices yields an array of lower rank
# row_r1 = a[1, :] 
# print(row_r1)
# # while using only slices yields an array of the same rank as the original array:
# row_r2 = a[1:2, :]
# print(row_r2)
# 可以print一下shape

# Integer array indexing: 
# When you index into numpy arrays using slicing, 
# the resulting array view will always be a subarray of the original array.
# In contrast, integer array indexing allows you to construct arbitrary arrays
# using the data from another array.
# a = np.array([[1,2], [3, 4], [5, 6]])
# print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
# # 这句的意思是：从数组中提取位置分别为：
# # a[0, 0] → 1
# # a[1, 1] → 4
# # a[2, 0] → 5
# # 等价于：
# print(np.array([a[0,0], a[1,1], a[2,0]]))
# # 重复提取某个元素：
# print(a[[0,0],[1,1]])
# # 等价于：
# print(np.array([a[0,1], a[0,1]])) # vs print(a[0,1], a[0,1])

# a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(a)
# b = np.array([0,2,0,1])
# # Select one element from each row of a using the indices in b
# print(a[np.arange(4), b])
# a[np.arange(4), b] += 10
# print(a)

# Boolean array indexing:
# a = np.array([[1,2], [3, 4], [5, 6]])
# print(a)
# bool_idx = (a > 2)
# print(bool_idx)
# print(a[bool_idx]) # this create an array with rank 1, equivalant to write a[a > 2]

# datatype:import numpy as np
# x = np.array([1, 2])   # Let numpy choose the datatype
# print(x.dtype)         # Prints "int64"
# x = np.array([1.0, 2.0])   # Let numpy choose the datatype
# print(x.dtype)             # Prints "float64"
# x = np.array([1, 2], dtype=np.int64)   # Force a particular datatype
# print(x.dtype)                         # Prints "int64"

# Array math 我似乎知道是怎么回事 似乎

# Broadcasting
# g老师说：NumPy 中的 broadcast（广播）允许不同形状的数组在进行算术运算时，自动对齐维度，
# 就像把小数组“扩展”成大数组一样，但实际上不复制数据，效率很高。
a = np.array([1, 2, 3])
b = 2
print(a + b)  # 输出: [3 4 5]。NumPy 会自动将 b 广播为 [2, 2, 2]
# 多维的例子：
A = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [4, 5, 6, 7],[4, 5, 6, 7]])
B = np.array([10, 20, 30, 40])
print(A + B)
# broadcast 的规则：
# 广播规则可以理解成从 后（右）往前 一位一位比较两个数组的 shape，按照下面的逻辑：
# 对于每个维度，要么两个维度大小一样，要么其中一个是 1，否则报错。
# 比如：
# A.shape = (3, 1)
#  B.shape = (1, 4)
# 最后一个维度：1 和 4， 有一个是 1，可以广播；
# 倒数第二个维度：3 和 1，  有一个是 1，可以广播；
# 所以可以广播，广播后：
# A 会变成 (3, 4)
# B 会变成 (3, 4)
