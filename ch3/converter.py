from lib.stack import Stack


def dec_to_bin(number, base):
    """
    >>> dec_to_bin(1, 2)
    '1'
    >>> dec_to_bin(2, 2)
    '10'
    >>> dec_to_bin(7, 2)
    '111'
    >>> dec_to_bin(15, 2)
    '1111'
    >>> dec_to_bin(15, 16)
    'F'
    """
    assert base <= 16, 'Max base = 16'
    digits = "0123456789ABCDEF"
    s = Stack()
    number_ = number
    while True:
        s.push(number_ % base)
        number_ = number_ // base
        if number_ == 0:
            break
    return ''.join(str(digits[s.pop()]) for _ in range(s.size()))
