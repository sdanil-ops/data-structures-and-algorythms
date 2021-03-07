#  Copyright (c) 2021. Danil Smirnov
#  zabanen.nu@ya.ru

def bubble_sort(unsorted_list):
    """sort list by bubble sort method"""
    swaps = True
    quantity_elements = len(unsorted_list)
    while swaps:
        swaps = False
        for bypass in range(1, quantity_elements):
            for k in range(0, quantity_elements - bypass):
                if unsorted_list[k] > unsorted_list[k + 1]:
                    swaps = True
                    unsorted_list[k], unsorted_list[k + 1] = unsorted_list[k + 1], unsorted_list[k]

def insertion_sort(usnsorted_list):
    """sort list by insertion sort method"""
    pass

def selection_sort(usnsorted_list):
    """sort list by selection sort method"""
    pass


def test_sort(sort_algorythm):
    print("Testing: ", sort_algorythm.__doc__)
    print("Testcase #1:", end="")
    unsorted_list = [4, 1, 3, 5, 6, 2, 7, 9, 0, 8]
    sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sort_algorythm(unsorted_list)
    print("Passed" if sorted_list == unsorted_list else "Failed")

    print("Testcase #2:", end="")
    unsorted_list = [0, 0, 0, 0, 0]
    sorted_list = [0, 0, 0, 0, 0]
    sort_algorythm(unsorted_list)
    print("Passed" if sorted_list == unsorted_list else "Failed")

    print("Testcase #3:", end="")
    unsorted_list = [0, -1, -3, -5, -7, -9, -2, -4, -6, -8]
    sorted_list = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
    sort_algorythm(unsorted_list)
    print("Passed" if sorted_list == unsorted_list else "Failed")

    print("Testcase #3:", end="")
    unsorted_list = list(range(5, 0, -1)) + list(range(10, 21)) + list(range(6, 10))
    sorted_list = list(range(1, 21))
    sort_algorythm(unsorted_list)
    print("Passed" if sorted_list == unsorted_list else "Failed")

if __name__ == "__main__":
    test_sort(bubble_sort)
    test_sort(insertion_sort)
    test_sort(selection_sort)
