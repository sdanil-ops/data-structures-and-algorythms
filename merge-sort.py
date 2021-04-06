#  -----------------------------------------------------------
#
#  simple demonstration of merge sort
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------
def merge(left: list, right: list):
    result = [0] * (len(left) + len(right))
    i = k = n = 0
    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            result[n] = left[i]
            i += 1
        else:
            result[n] = right[k]
            k += 1
        n += 1
    while i < len(left):
        result[n] = left[i]
        i += 1
        n += 1
    while k < len(right):
        result[n] = right[k]
        k += 1
        n += 1
    return result


def merge_sort(array: list):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)



def test_sort(test):
    print('Testing merge sort')

    print('Testcase #1: ', end='')
    test_case = test([100, 10, 5, 13, 33, 60, 6, 55, 99, 0])
    sorted_array = [0, 5, 6, 10, 13, 33, 55, 60, 99, 100]
    print('Ok' if test_case == sorted_array else 'No')

    print('Testcase #2: ', end='')
    test_case = test(list(range(5, 0, -1)) + list(range(10, 21)) + list(range(6, 10)))
    sorted_array = list(range(1, 21))
    print('Ok' if test_case == sorted_array else 'No')

    print('Testcase #3: ', end='')
    test_case = test([-1, -2, -3, -5, 0, 0, -4, 3, 2, 1])
    sorted_array = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3]
    print('Ok' if test_case == sorted_array else 'No')


if __name__ == '__main__':
    test_sort(merge_sort)
