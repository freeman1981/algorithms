from lib.dequeue import Deque


def is_pallindrome(input_str):
    """
    >>> is_pallindrome('abba')
    True
    >>> is_pallindrome('aba')
    True
    >>> is_pallindrome('abac')
    False
    >>> is_pallindrome('')
    True
    >>> is_pallindrome('a')
    True
    """
    dq = Deque.from_iterable(input_str)
    still_equal = True
    while dq.size() > 1 and still_equal:
        if dq.remove_front() != dq.remove_rear():
            still_equal = False
    return still_equal
