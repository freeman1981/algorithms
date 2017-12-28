from algorithms.lib.stack import Stack


def par_check(test_str: str) -> bool:
    """
    >>> par_check('(()')
    False
    >>> par_check(')')
    False
    >>> par_check(')(')
    False
    >>> par_check('()()')
    True
    >>> par_check('(()())')
    True
    >>> par_check('((++)(--)**)')
    True
    """
    par_s = Stack()
    for ch in test_str:
        if ch == '(':
            par_s.push(ch)
        elif ch == ')':
            if par_s.is_empty():
                return False
            par_s.pop()
    return par_s.is_empty()
