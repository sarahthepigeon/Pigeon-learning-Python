NumPy数组确实有很多强大且"神奇"的功能，这里介绍一些最有用的：

## 广播机制 (Broadcasting)
不同形状的数组可以直接进行运算：
```python
import numpy as np

a = np.array([[1, 2, 3]])     # 形状 (1, 3)
b = np.array([[4], [5], [6]]) # 形状 (3, 1)
result = a + b                # 自动广播为 (3, 3)
```

## 向量化运算
整个数组的运算比循环快得多：
```python
# 传统方式
result = []
for x in range(1000000):
    result.append(x ** 2)

# NumPy方式
arr = np.arange(1000000)
result = arr ** 2  # 快几十倍
```

## 花式索引
使用数组作为索引：
```python
arr = np.array([10, 20, 30, 40, 50])
indices = np.array([0, 2, 4])
print(arr[indices])  # [10 30 50]

# 二维数组的高级索引
matrix = np.random.rand(5, 5)
rows = [0, 2, 4]
cols = [1, 3, 0]
print(matrix[rows, cols])  # 取出特定位置的元素
```

## 布尔索引
用条件直接筛选数据：
```python
arr = np.array([1, 5, 3, 8, 2, 9])
mask = arr > 4
print(arr[mask])  # [5 8 9]

# 复杂条件
print(arr[(arr > 2) & (arr < 8)])  # [5 3]
```

## 形状变换的灵活性
```python
arr = np.arange(12)
print(arr.reshape(3, 4))    # 变成3x4矩阵
print(arr.reshape(-1, 3))   # -1表示自动计算维度
print(arr[:, np.newaxis])   # 增加新轴
```

## 通用函数 (ufunc)
对整个数组元素级操作：
```python
arr = np.array([1, 4, 9, 16])
print(np.sqrt(arr))         # 开方
print(np.sin(arr))          # 三角函数
print(np.where(arr > 5, arr, 0))  # 条件替换
```

## 内存视图
不复制数据的切片操作：
```python
original = np.arange(10)
view = original[::2]        # 每隔一个元素
view[0] = 999              # 修改view也会影响original
```

## 线性代数运算
```python
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)

# 矩阵乘法
C = A @ B  # 或 np.dot(A, B)

# 特征值分解
eigenvals, eigenvecs = np.linalg.eig(A)

# 求逆矩阵
inv_A = np.linalg.inv(A)
```

## 数组拼接和分割
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 拼接
combined = np.concatenate([a, b])
stacked = np.stack([a, b])  # 堆叠

# 分割
parts = np.split(combined, 2)
```

## 内存高效的操作
```python
# 原地操作，不创建新数组
arr += 5          # 比 arr = arr + 5 更节省内存
np.add(arr, 5, out=arr)  # 显式指定输出位置
```

这些功能让NumPy不仅运行速度快，而且代码简洁优雅。掌握这些特性能让你的数据处理效率大大提升！