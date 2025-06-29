# 这个代码用来生成比`limit`小的质数列表

def prime_list_helper(n, prime_list):
	# 给定一个正整数n和目前的质数列表prime_list，
	# 返回一个布尔值，表示n是否是质数
	# prerequisite: n >= 2, prime_list 包含所有小于等于sqrt(n)的质数
	for prime in prime_list:
		if prime * prime > n:
			break
		if n % prime == 0:
			return False
	return True

def create_prime_list(limit):
	prime_list = []
	for n in range(2, limit):
		if prime_list_helper(n, prime_list):
			prime_list.append(n)
	return prime_list

def store_prime_list(prime_list, filename):
	with open(filename, 'w') as f:
		for prime in prime_list:
			f.write(f"{prime}\n")

def main():
	limit = int(1e6)
	prime_list = create_prime_list(limit)
	store_prime_list(prime_list, 'prime_list.txt')

if __name__ == "__main__":
	main()