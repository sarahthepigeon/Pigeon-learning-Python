## Python列表小练习

今天的任务简单一点哈哈哈。要求在一个while循环里不停地输入整数，每次输入完一个数字都打印一下列表的长度、最大值、最小值、平均值和中位数。
有以下规则：
1. 输入的数字必须是整数，方便起见，如果不是整数就直接报错（不做try...except...）
2. 如果输入了"q"，就退出循环
3. 不允许输入重复的数字，如果输入了重复的数字就提醒用户，但是不报错也不退出循环，然后prompt用户重新输入
4. 最后对列表进行从大到小排序，并打印出来

下面是一个示例：
```
请输入一个整数，输入q退出: 1
长度 1, 最大值 1, 最小值 1, 平均值 1.0
---
请输入一个整数，输入q退出: 2
长度 2, 最大值 2, 最小值 1, 平均值 1.5
---
请输入一个整数，输入q退出: 3
长度 3, 最大值 3, 最小值 1, 平均值 2.0
---
请输入一个整数，输入q退出: q
循环结束，从大到小排序的列表：[3, 2, 1]

Process finished with exit code 0
```

示例2：
```
请输入一个整数，输入q退出: 100
长度 1, 最大值 100, 最小值 100, 平均值 100.0
---
请输入一个整数，输入q退出: -100
长度 2, 最大值 100, 最小值 -100, 平均值 0.0
---
请输入一个整数，输入q退出: I love pigeons
Traceback (most recent call last):
  File "C:\Users\IWMAI\OneDrive\Programs\Python\Pigeon-learning-Python\Day3\Day3.py", line 27, in <module>
    main()
    ~~~~^^
  File "C:\Users\IWMAI\OneDrive\Programs\Python\Pigeon-learning-Python\Day3\Day3.py", line 10, in main
    num = int(num)
ValueError: invalid literal for int() with base 10: 'I love pigeons'

Process finished with exit code 1
```

今天Pretty Chill。加油Sarah！
