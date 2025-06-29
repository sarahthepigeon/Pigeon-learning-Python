# 今天的作业就写在这个文档里吧
import sys

def load_prime_list(filename):
	prime_list = []
	try:
		with open(filename, 'r') as f:
			for line in f:
				prime_list.append(int(line.strip()))
		return prime_list
	except FileNotFoundError:
		print(f"文件 {filename} 不存在，请先生成质数列表。")
		sys.exit(1)

def is_prime(n, prime_list):
	# 给定一个正整数n，判断它是否是质数
	if n < 2:
		return False
	for prime in prime_list:
		if prime * prime > n:
			break
		if n % prime == 0:
			return False
	return True

def main():
	# 首先，加载质数列表
	prime_list = load_prime_list('prime_list.txt')
	# 手动设置可以检测的数字上限为质数列表中的最大值平方
	limit = prime_list[-1] ** 2

	n = input("请输入一个正整数：")
	if (not n.isdecimal()) or int(n) <= 0:
		print("输入的不是正整数")
		return
	n = int(n)

	if n > limit:
		print(f"输入的数字 {n} 超过了检测范围 {limit}，请重新输入一个较小的正整数。")
		return

	if is_prime(n, prime_list):
		print(n, "是质数")
	else:
		print(n, "不是质数")


if __name__ == "__main__":
	main()