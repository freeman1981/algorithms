def list_sum(list_):
    """
    >>> list_sum([1,2,3])
    6
    """
    return sum(list_)


def list_sum_2(list_):
    """
    >>> list_sum([1,2,3])
    6
    """
    sum_ = 0
    for i in list_:
        sum_ += i
    return sum_


def list_sum_3(list_):
    """
    >>> list_sum([1,2,3])
    6
    """
    if len(list_) == 1:
        return list_[0]
    else:
        return list_[0] + list_sum_3(list_[1:])
