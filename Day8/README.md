## Day 8: enumerate和zip练习

今天要学的是两个很好用的小技巧。

# 1. enumerate函数
可以让你在遍历列表的时候顺便获取索引，很好用。

```python
my_words = ["Seagull", "loves", "Pigeon"]
for index, word in enumerate(my_words):
	print(f"Index: {index}: {word}")
```

这里涉及到一个python中的自动解包的知识。自动解包是指你可以使用相等数量的变量来接受一个可迭代对象中的元素。比如说：

```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple

my_list = [4, 5, 6]
d, e, f = my_list
```

你可以试试`type(enumerate(my_words))`和`help(enumerate)`。你需要往里面传递一个可迭代对象，它返回的也是一个可迭代对象。

我们假设如果去迭代`my_words`（which means `for word in my_words`）每一轮迭代得到的word是string类型的话;

同样地，迭代`enumerate(my_words)`每一轮迭代得到的word是一个tuple类型，tuple的第一个元素是索引，第二个元素是原来的word。

```Python
my_words = ["Seagull", "misses", "pigeon", "..."]
for xxx in enumerate(my_words):
    print(xxx)
# (0, 'I')
# (1, 'miss')
# (2, 'Sarah')
# (3, '...')
```

```python
my_words = ["I", "miss", "Sarah"]
# 所以这个
for index, word in enumerate(my_words):
    print(f"Index: {index}: {word}")
# 等价于
for i in range(len(my_words)):
    print(f"Index: {i}: {my_words[i]}")
```

哦对，enumerate函数还可以传第二个参数`start`，用来指定索引的起始值。

```python
my_words = ["I", "really", "miss", "Sarah", "🥺🥺🥺"]
for index, word in enumerate(my_words, start=1):
    print(f"Index: {index}: {word}")
# Index: 1: I
# Index: 2: really
# Index: 3: miss
# Index: 4: Sarah
# Index: 5: 🥺🥺🥺
```

# 2. zip函数

zip函数可以让你同时遍历多个列表。它会把多个可迭代对象打包成一个个元组。常见的用法是同时遍历两个列表。
举个例子当你有一个列表存储x坐标，另一个列表存储y坐标，你可以这样做：

```python
x_coords = [1, 2, 3]
y_coords = [4, 5, 6]
for x, y in zip(x_coords, y_coords):
    print(f"Point: ({x}, {y})")
```

（当然也等同于）
```python
x_coords, y_coords = [1, 2, 3], [4, 5, 6]  # note 这里也用到了自动解包
for i in range(len(x_coords)):
    print(f"Point: ({x_coords[i]}, {y_coords[i]})")
```

（也等同于）
```python
x_coords, y_coords = [1, 2, 3], [4, 5, 6]
for coords in zip(x_coords, y_coords):
    print(f"Point: ({coords[0]}, {coords[1]})")
```

zip函数也可以接受多个可迭代对象，如果它们的长度不一样，zip会在最短的那个可迭代对象结束时停止。

```python
x_coords = [1, 2, 3]
y_coords = [4, 5]
for x, y in zip(x_coords, y_coords):
    print(f"Point: ({x}, {y})")
# Point: (1, 4)
# Point: (2, 5)
```

今天要学的就是这么多！东西还挺多的，建议你花半个小时到一个小时来消化一下。明天我应该会教你Jupyter Notebook，这是一个很有用的学习和实验的工具。

加油Sarah，希望你能对Python提起兴趣！
