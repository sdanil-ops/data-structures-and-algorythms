#  -----------------------------------------------------------
#
#  simple demonstration of quick sort 
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------

def quick_sort(array):
    if len(array) < 2:
        return array
    rod = array[0]
    left = [i for i in array[1:] if i <= rod]
    right = [i for i in array[1:] if i > rod]
    return quick_sort(left) + [rod] + quick_sort(right)


def test_sort(test):
    print('Testing quick sort')

    print('Testcase #1: ', end='')
    test_case = test([10, 5, 13, 33])
    sorted_array = [5, 10, 13, 33]
    print('Ok' if test_case == sorted_array else 'No')

    print('Testcase #2: ', end='')
    test_case = test(list(range(5, 0, -1)) + list(range(10, 21)) + list(range(6, 10)))
    sorted_array = list(range(1, 21))
    print('Ok' if test_case == sorted_array else 'No')

    print('Testcase #3: ', end='')
    test_case = test([-1, -2, -3, 3, 2, 1])
    sorted_array = [-3, -2, -1, 1, 2, 3]
    print('Ok' if test_case == sorted_array else 'No')


if __name__ == '__main__':
    test_sort(quick_sort)
