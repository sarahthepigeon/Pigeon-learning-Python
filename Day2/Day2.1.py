import sys

while 1:
    method = input("""请选择转换方式：
1. 摄氏度转华氏度
2. 华氏度转摄氏度
请输入你的选择（1或2）：
    """)

    if method == "1":
        temp_c = input("请输入一个摄氏度的温度：")
        try:
            temp_c = float(temp_c)
        except ValueError:
            print("请只输入整数或者浮点数")
            sys.exit()

        if isinstance(temp_c, float):
            if temp_c >= -273.15:
                temp_f = float(temp_c) * 9 / 5 + 32
                print(f"{temp_f:.2f}")
            else:
                print("输入温度太低，不合理")

    elif method == "2":
        temp_f = input("请输入一个华氏度的温度：")
        try:
            temp_f = float(temp_f)
        except ValueError:
            print("请只输入整数或者浮点数")
            sys.exit()

        if isinstance(temp_f, float):
            if temp_f >= -459.67:
                temp_c = (float(temp_f) - 32) / 9 * 5
                print(f"{temp_c:.2f}")
            else:
                print("输入温度太低，不合理")

    else:
        print("输入错误，请输入1或2")

    print("---")



