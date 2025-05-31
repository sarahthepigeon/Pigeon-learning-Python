import sys

print("请选择转换方式：")
print("1. 摄氏度转华氏度")
print("2. 华氏度转摄氏度")
choice = input("请输入你的选择（1或2）：")

if choice == "1":
	# 摄氏度转华氏度
	celsius = input("请输入一个摄氏度的温度：")
	try:
		celsius = float(celsius)
	except ValueError:
		print("请只输入整数或者浮点数")
		sys.exit(0)
	if celsius < -273.15:
		print("输入温度太低，不合理")
		sys.exit(0)
	fahrenheit = celsius * 9/5 + 32
	print(fahrenheit)

elif choice == "2":
	# 华氏度转摄氏度
	fahrenheit = input("请输入一个华氏度的温度：")
	try:
		fahrenheit = float(fahrenheit)
	except ValueError:
		print("请只输入整数或者浮点数")
		sys.exit(0)
	if fahrenheit < -459.67:
		print("输入温度太低，不合理")
		sys.exit(0)
	celsius = (fahrenheit - 32) * 5/9
	print(celsius)

else:
	print("输入错误，请输入1或2")
	sys.exit(0)