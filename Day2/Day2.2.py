import sys

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def validate_celsius_input(celsius):
    # 输入整数或浮点数，验证是否 >= 0K
	return celsius >= -273.15

def validate_fahrenheit_input(fahrenheit):
    # 输入整数或浮点数，验证是否 >= 0K
	return fahrenheit >= -459.67

def main():
    while 1:
        method = input("""请选择转换方式：
1. 摄氏度转华氏度
2. 华氏度转摄氏度
请输入你的选择（1或2）：""")
        if method == "1":
            temp_c = input("请输入一个摄氏度的温度：")
            try:
                temp_c = float(temp_c)
            except ValueError:
                print("请只输入整数或者浮点数")
                sys.exit()
            if(validate_celsius_input(temp_c)):
                temp_f = celsius_to_fahrenheit(temp_c)
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
            if (validate_fahrenheit_input(temp_f)):
                temp_c = fahrenheit_to_celsius(temp_f)
                print(f"{temp_c:.2f}")
            else:
                print("输入温度太低，不合理")
        else:
            print("输入错误，请输入1或2")

        print("---")

main()

