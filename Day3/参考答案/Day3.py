def main():
	num_list = []

	while True:
		num = input("请输入一个整数，输入q退出: ")

		if num == "q":
			break

		num = int(num)

		if num_list.count(num) != 0:
			print(f"{num} 已经存在于列表中")
			continue

		num_list.append(num)

		print(f"长度 {len(num_list)}, 最大值 {max(num_list)}, 最小值 {min(num_list)}, 平均值 {sum(num_list) / len(num_list)}")
		print("---")

	# 循环结束，打印从大到小sort好的列表
	num_list.sort(reverse=True)
	# num_list = sorted(num_list, reverse=True)  # 也可以这样写
	print(f"循环结束，从大到小排序的列表：{num_list}")

if __name__ == "__main__":
	main()