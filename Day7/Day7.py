# 列表推导式： list = [表达式 for i in 可迭代对象]
# 可以处理if else语句，可以处理字符串，可以嵌套多层循环结构, 可以加多个变量
List = [(x,y) for x in range(10) if x % 2 == 0 for y in range(6) if y % 2 != 0] # if else是筛选用的，所以放在for的后面
List = ["happy" if i % 2 == 0 else "pigeon" for i in range(10)] # if else 属于表达式的一部分，需要写在for之前
# g老师给的例子：
list1 = list(range(1, 101))
list2 = list(range(1, 51))
result = [f(x, y)       # ← expression
  for x in list1       # ← for clause 1
  for y in list2       # ← for clause 2 (嵌套)
  if x + y > 50        # ← condition 1
  if x != y            # ← condition 2
]

# 等价于：
result = []
for x in list1:
    for y in list2:
        if x + y > 10:
            if x != y:
                result.append(f(x, y))

# 单行if语句
# Python的单行 if else 不支持 elif，但是可以用多层if else嵌套写
for x in range(10):
    y = "greater than 5" if x > 5 else "equals 5" if x == 5 else "less than 5"
    # 在print中也可以加if else结构
    print(f"{x} {y}" if x == 5 else f"{x} is {y}")
    # 或者把line 26 和 28 合并成：
    # print(f"{x} equals 5" if x == 5 else f"{x} is greater than 5" if x > 5 else f"{x} is less than 5")


week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for day in week:
    print("Weekend" if day in ["saturday", "sunday"] else "weekday")

#有关于带有tuple的list，for循环可以直接这么写：
# List = [(0, "hi"), (1, "there"), (2, "my"), (3, "pigeon")]
# for i, x in List:
#     print(f"{i}: {x}")
# 输出的结果是：
# 0: hi
# 1: there
# 2: my
# 3: pigeon

