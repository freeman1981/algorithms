from lib.stack import Stack


par = {'(': ')', '{': '}', '[': ']'}


open_par = par.keys()
close_par = par.values()


def par_check(test_str: str) -> bool:
    """
    >>> par_check('(()')
    False
    >>> par_check(')')
    False
    >>> par_check(')(')
    False
    >>> par_check('()(}')
    False
    >>> par_check('([]{})')
    True
    >>> par_check('[(++){--}**]')
    True
    """
    par_s = Stack()
    for ch in test_str:
        if ch in open_par:
            par_s.push(ch)
        elif ch in close_par:
            if par_s.is_empty():
                return False
            if par[par_s.pop()] != ch:
                return False
    return par_s.is_empty()
