def merge(a: list, b: list):
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


# def merge_sort(a):
#     if len(a) <= 1:
#         return
#     middle = len(a) // 2
#     l = [a[i] for i in range(0, middle)]
#     r = [a[i] for i in range(middle, len(a))]
#     merge_sort(l)
#     merge_sort(r)
#     c = merge(l, r)
#     for i in range(len(a)):
#         a[i] = c[i]


def merge_sort(a):
    len_a = len(a)
    if len_a <= 1:
        return
    middle = len_a // 2
    l = a[:middle]
    r = a[middle:]
    merge_sort(l)
    merge_sort(r)
    c = merge(l, r)
    a[:] = c[:]


def hoar_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    l, m, r = [], [], []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    hoar_sort(l)
    hoar_sort(r)
    k = 0
    for x in l + m + r:
        a[k] = x
        k += 1


def check_sorted(a, ascending=True):
    k = 1 if ascending else -1
    # k = 2 * int(ascending) - 1
    for i in range(0, len(a) - 1):
        if (a[i + 1] - a[i]) * k < 0:
            return False
    return True


a = [5, 4, 1, 3]
b = a[:]
c = a[:]

merge_sort(a)
hoar_sort(b)
c.sort()

print(*a)
print(*b)
print(*c)
print(check_sorted(c))
print(check_sorted(c, ascending=False))
