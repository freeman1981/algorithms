def move_tower(height, a, b, c):
    if height == 0:
        return
    move_tower(height - 1, a, c, b)
    move_disk(a, b)
    move_tower(height - 1, c, b, a)


def move_disk(fp, tp):
    print('move from {} to {}'.format(fp, tp))


move_tower(3, 'A', 'B', 'C')
