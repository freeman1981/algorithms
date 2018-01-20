def hanoi(n, a, b, c):
    if n <= 0:
        return
    hanoi(n - 1, a, c, b)
    print('from', a, 'to', b)
    hanoi(n - 1, c, b, a)


hanoi(2, 'A', 'B', 'C')
