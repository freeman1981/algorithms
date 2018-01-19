from collections import deque


def convert(number, base):
    """
    >>> convert(10, 10)
    '10'
    >>> convert(2, 2)
    '10'
    >>> convert(16, 16)
    '10'
    >>> convert(15, 16)
    'F'
    """
    digits = '0123456789ABCDEF'
    if number < base:
        return digits[number]
    else:
        return convert(number // base, base) + digits[number % base]


def reverse(string):
    """
    >>> reverse('123')
    '321'
    >>> reverse('1')
    '1'
    >>> reverse('')
    ''
    """
    if len(string) <= 1:
        return string
    else:
        return string[-1] + reverse(string[:-1])


def is_palindrome(string):
    """
    >>> is_palindrome('123')
    False
    >>> is_palindrome('1')
    True
    >>> is_palindrome('')
    True
    """
    q = deque(string)
    if len(q) <= 2:
        return True
    return q.popleft() == q.pop() and is_palindrome(''.join(q))
