from lib.stack import Stack


def dec_to_bin(number):
    """
    >>> dec_to_bin(1)
    '1'
    >>> dec_to_bin(2)
    '10'
    >>> dec_to_bin(7)
    '111'
    >>> dec_to_bin(15)
    '1111'
    """
    s = Stack()
    number_ = number
    while True:
        s.push(number_ % 2)
        number_ = number_ // 2
        if number_ == 0:
            break
    return ''.join(str(s.pop()) for _ in range(s.size()))


def dec_to_bin_alt(number):
    """
    >>> dec_to_bin_alt(1)
    '1'
    >>> dec_to_bin_alt(2)
    '10'
    >>> dec_to_bin_alt(7)
    '111'
    >>> dec_to_bin_alt(15)
    '1111'
    """
    return bin(number).lstrip('0b')
