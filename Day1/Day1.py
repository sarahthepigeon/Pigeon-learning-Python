temp_c = input("请输入一个摄氏度的温度")
try:
    temp_c = float(temp_c)
except ValueError:
    print("请只输入整数或者浮点数")

if isinstance(temp_c, float) or isinstance(temp_c, int):
    if temp_c >= -273.15:
        temp_f = float(temp_c) * 9 / 5 + 32
        print(f"{temp_f:.2f}")
    else:
        print("输入温度太低，不合理")

