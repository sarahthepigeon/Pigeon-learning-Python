def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, n):  # 也可以写成 range(2, int(n**0.5) + 1)
		if n % i == 0:
			return False
	return True

def main():
	n = input("请输入一个正整数：")
	if (not n.isdecimal()) or int(n) <= 0:
		print("输入的不是正整数")
		return
	n = int(n)

	if is_prime(n):
		print(n, "是质数")
	else:
		print(n, "不是质数")

main()

# 提示：有一个比较大的质数是 100000007，还有一个比较大的质数是 2147483647