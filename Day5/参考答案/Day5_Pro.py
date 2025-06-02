# 这是更复杂的版本，灵活性会稍微高一些，但是emmm好像有点过于复杂了。有的时候面对简单的任务我们更应该写简单的代码。
# 你看看即可，不必掌握

import math
from typing import Iterator

def gen_wave(num_lines, line2x, wave_func, y2chars) -> Iterator[str]:
	"""
	Generate a wave pattern based on the number of lines, line to x mapping, and y to amplitude mapping.

	Args:
		num_lines (int): Number of lines in the wave.
		line2x (function): A function that maps line indices to x coordinates.
		wave_func (function): A function that defines the wave pattern.
		y2chars (function): A function that maps y coordinates to characters.

	Yields:
		str: A string representing the wave pattern for each line.
	"""
	for i in range(num_lines):
		x = line2x(i)
		y = wave_func(x)
		yield y2chars(y)

def main():
	# Define the wave parameters
	num_lines = 1000
	line2x = lambda i: 2 * math.pi / 100 * i  # mapping line index to x coordinate
	wave_func = lambda x: -math.cos(x)  # wave function (sine wave)
	def y2chars(y):
		num_chars = round((y + 1) / 2 * 25 + 1)  # mapping y coordinate to characters
		assert 1 <= num_chars <= 26, "Number of characters must be between 1 and 26"
		return "abcdefghijklmnopqrstuvwxyz"[:num_chars]

	# save to file
	with open("wave.txt", "w") as f:
		for line in gen_wave(num_lines, line2x, wave_func, y2chars):
			f.write(line + "\n")

main()