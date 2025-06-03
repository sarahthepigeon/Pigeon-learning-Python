import math
import numpy
import string

alphabet = list(string.ascii_lowercase)

def print_alphabet(n):
    if n == 0:
        print("a")
        return
    for i in range(n):
        print(alphabet[i], end = "")
    print("")
    return

def main():
    print(alphabet)
    for i in range(1000):
        # 每一行的长度n：
        n = int(26 * (1 + numpy.cos(2 * math.pi * (i % 100) / 100)) / 2)
        print_alphabet(n)

main()

