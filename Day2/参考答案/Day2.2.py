# 注：一般我们编写函数秉承着“单一职责原则”，即一个函数只做一件事，并且做好这件事。
# 不过说实在的，程老师也不确定哪种对函数分类的方法更好，只能说实践出真知吧，多试一试哈哈哈
# 比如说你也可以把validate函数写在convert函数里面，或者你也可以专门写一个函数循环询问用户输入温度值，直到输入正确为止。

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
	print("请选择转换方式：")
	print("1. 摄氏度转华氏度")
	print("2. 华氏度转摄氏度")
	choice = input("请输入你的选择（1或2）：")

	if choice == "1":
		celsius = input("请输入一个摄氏度的温度：")
		try:
			celsius = float(celsius)
		except ValueError:
			print("请只输入整数或者浮点数")
			return
		if not validate_celsius_input(celsius):
			print("输入温度太低，不合理")
			return
		fahrenheit = celsius_to_fahrenheit(celsius)
		print(fahrenheit)
	
	elif choice == "2":
		fahrenheit = input("请输入一个华氏度的温度：")
		try:
			fahrenheit = float(fahrenheit)
		except ValueError:
			print("请只输入整数或者浮点数")
			return
		if not validate_fahrenheit_input(fahrenheit):
			print("输入温度太低，不合理")
			return
		celsius = fahrenheit_to_celsius(fahrenheit)
		print(celsius)

	else:
		print("输入错误，请输入1或2")
		return

main()