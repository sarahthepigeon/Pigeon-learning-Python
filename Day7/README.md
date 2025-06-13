## Day 7: 让我们focus more on Python基础

Python基础有一些方便的功能，但是如果一天只学一个功能未免太少了一点。我们要不把每天的任务分成几个小功能来学习。

可能有一些知识点不用你动手实操，我写在这里就行了。

## 1. f-string
想必你也知道，f-string是一个很好用的format字符串的方式，学会了它基本就不需要学别的format方法了。

```python
name = "Sarah"
age = 20
print(f"My name is {name}, I am {age} years old.")
```

除此之外，print支持传递`end`和`sep`参数来控制输出的结尾和分隔符。

```python
print("Hello", "World", end="!")
print("Hello", "World", sep="-")
# 输出:
# Hello World!Hello-World
```

## 2. 列表推导式
列表推导式很强大，能把一个for循环塞进一行代码。举个例子：

```python
# before
squares = []
for i in range(10):
    squares.append(i * i)
# after
squares = [i * i for i in range(10)]
```

你还可以往里面加if

```python
# before
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i * i)
# after
squares = [i * i for i in range(10) if i % 2 == 0]
```

# 3. 单行if语句
单行if语句可以让代码更简洁。比如：

```python
x = 10 # 或者一个别的数

# before
if x > 5:
    y = "大于5"
else:
    y = "小于等于5"
# after
y = "大于5" if x > 5 else "小于等于5"
# ("大于5" if x > 5 else "小于等于5") 整体作为一个表达式赋值给y
```

另外，if语句也可以单行写，means，如果if语句后面只有一行代码，可以将这行代码和if语句放在同一行。

```python
x = 10
if x > 5: print("x is greater than 5")
else: print("x is not greater than 5")
```

嗯嗯，今天先学这么多吧，也不少了哈哈哈。

regarding作业……我想请你多试一试这些语句的写法，并探索special cases。举个例子，你可能会好奇列表推导式的最抽象的结构是什么，核心是什么……

像上面的单行代码在很多情况下是很有用的。如果你熟悉了这些用法就会觉得Python比C/C++更方便。比如：

```python
a = [f"i={i}, j={j}" for i in range(3) for j in range(3)]

if a == 1: print("a is 1")
else: print("a is not 1")

print("Hello", "World", sep=", ", end="!\n")

x = 10  # 或者一个别的数
y = "大于5" if x > 5 else "等于5" if x == 5 else "小于5"
```

请你在python console里练习这些语法，然后把你觉得有趣的例子写下来吧。可以写到此文件中，也可以写到.py文件或者.txt文件中。

明天你想学什么？想学jupyter notebook吗，还是想学更多Python基础比如enumerate和zip？