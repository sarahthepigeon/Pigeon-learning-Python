def is_prime(n):
    # 一些逻辑
    for i in range(2, n):
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