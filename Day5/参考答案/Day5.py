import math

def gen_wave():
	ans = []  # list里面的每一个元素是一行字符串
	for i in range(1000):
		x = 2 * math.pi / 100 * i
		y = -math.cos(x)
		num_chars = round((y + 1) / 2 * 25 + 1)
		assert 1 <= num_chars <= 26, "Number of characters must be between 1 and 26"
		ans.append("abcdefghijklmnopqrstuvwxyz"[:num_chars])
	return ans

# generate the pattern and save to file
with open("wave.txt", "w") as file:
	lines = gen_wave()
	for line in lines:
		file.write(line + "\n")
