# -*- coding:utf-8 -*-
# find max sub array with digui

def FIND_MAX_CROSSING_SUBARRAY(data, first_index, median_index, last_index):
    left_sum = -99
    digit_sum = 0
    left_index = right_index = 0
    for i in range(median_index, first_index - 1, -1):
        digit_sum = digit_sum + data[i]
        if digit_sum > left_sum:
            left_sum = digit_sum
            left_index = i
    right_sum = -99
    digit_sum = 0
    for i in range(median_index + 1, last_index + 1):
        digit_sum = digit_sum + data[i]
        if digit_sum > right_sum:
            right_sum = digit_sum
            right_index = i
    return left_index, right_index, left_sum + right_sum


def FIND_MAXIMUN_SUBARRAY(data, low, high):
    if low == high:
        return low, high, data[low]
    else:
        (left_low, left_high, left_sum) = FIND_MAXIMUN_SUBARRAY(data, low, (low + high) / 2)
        (right_low, right_high, right_sum) = FIND_MAXIMUN_SUBARRAY(data, (low + high) / 2 + 1, high)
        (cross_low, cross_high, cross_sum) = FIND_MAX_CROSSING_SUBARRAY(data, low, (low + high) / 2, high)
        if (left_sum >= right_sum) and (left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def READ_FILE_DATA(filename):
    import re
    data = []
    with open(filename) as f:
        content = f.read()
        content.strip()
    temp = re.split(" ", content)
    for i in range(len(temp)):
        data.append(int(temp[i]))
    return data


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100)
    data = READ_FILE_DATA('data.txt')
    print data, '\n', sum(data), len(data)
    (left_index, right_index, digit_sum) = FIND_MAXIMUN_SUBARRAY(data, 0, len(data) - 1)
    print left_index, right_index, digit_sum
    print data[left_index], data[right_index]
