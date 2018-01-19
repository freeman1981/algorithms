def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
        return
    for digit in '0', '1':
        gen_bin(m - 1, prefix + digit)


def generate_number(n: int, m: int, prefix=None):
    """Генерирует все числа (с лидирующими нулями) в n-ричной системе счисления (n <= 10) длины m"""
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_number(n, m - 1, prefix)
        prefix.pop()


def generate_permutations(n: int, m: int=-1, prefix=None):
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='')
        return
    for number in range(1, n + 1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


# gen_bin(3)
# generate_number(3, 3)
generate_permutations(5)
