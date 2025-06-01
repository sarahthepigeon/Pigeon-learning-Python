import sys
def number_exist(my_list, n):
    for i in range(len(my_list)):
        if n == my_list[i]:
            return True
    else:
        return False

def update_list(my_list, n):  # update my_list in order
    if len(my_list) == 0:
        my_list.append(n)
        print(len(my_list))
        print(my_list)
        return my_list

    for i in range(len(my_list)):
        if n > my_list[i]:
            my_list.insert(i, n)
            return my_list
        else:
            my_list.append(n)

    print(my_list)
    return my_list

def update_max_value(n, max_value):
    if n > max_value:
        return n
    else :
        return max_value

def update_min_value(n, min_value):
    if n < min_value:
        return n
    else :
        return min_value

def calculate_avg(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    avg = sum / len(list)
    return avg

def main():
    max_value = float('-inf')  # Smallest possible number
    min_value = float('inf')  # Largest possible number
    my_list = []
    while 1:
        n = input("请输入一个整数，输入q退出:")
        if n == "q":
            break

        n = int(n)
        if number_exist(my_list, n):
            print(f"{n} 已经存在于列表中")

        else:
            # update my_list and related values
            my_list = update_list(my_list, n)
            length = len(my_list)
            max_value = update_max_value(n, max_value)
            min_value = update_min_value(n, min_value)
            avg = calculate_avg(my_list)
            print(f"长度 {length}, 最大值 {max_value}, 最小值 {min_value}, 平均值 {avg:.1f}")

        print("---")

    print(f"循环结束，从大到小排序的列表：{my_list}")
    sys.exit()

main()
