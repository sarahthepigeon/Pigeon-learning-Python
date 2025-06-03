import math
import numpy
import string

alphabet = list(string.ascii_lowercase)

def create_single_line(n):
    if n == 0:
        return 'a\n'
    else:
        line = ''
        for i in range(n):
            line += alphabet[i]
        line += '\n'
    return line

def update_cosine_list(line, cosine_list):
    cosine_list.append(line)
    return cosine_list

def main():
    cosine_list = []
    for i in range(1000):
        # 每一行的长度n：
        n = int(26 * (1 + numpy.cos(2 * math.pi * (i % 100) / 100)) / 2)
        cosine_list = update_cosine_list(create_single_line(n), cosine_list)

    for i in range(1000):
        with open("output.txt", "w") as f:
            f.writelines(cosine_list)

main()

