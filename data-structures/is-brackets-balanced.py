#  -----------------------------------------------------------
#  a simple demonstration of how a stack helps to determine 
#  are brackets  correctly placed in a sentence
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------
from stack import Stack

def remove_chars(string: str) -> str:
    brackets = {'(', '{', '[', ']', '}', ')'}
    result = ''
    for char in string:
        if char in brackets:
            result += char

    return result


def is_valid(string: str) -> bool:
    stack = Stack()
    brackets = {'(', '{', '['}
    string = remove_chars(string)
    for char in string:
        if char in brackets:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            top = stack.pop()
            if top == '(' and char != ')' or top == '[' and char != ']' or top == '{' and char != '}':
                return False
    return stack.is_empty()


def test_validator(test):
    test_1 = test('(test){test}(test[{test}]test)')  # True
    test_2 = test('{t(e(s)t[t]e{s}t}')  # False
    test_3 = test('just string without brackets')  # True
    print('Testing...')

    print('Testcase #1:', end='')
    print('Passed' if test_1 else 'Failed')

    print('Testcase #2:', end='')
    print('Failed' if test_2 else 'Passed')

    print('Testcase #3:', end='')
    print('Passed' if test_3 else 'Failed')


if __name__ == "__main__":
    test_validator(is_valid)
