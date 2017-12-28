from lib.queue import Queue


def play(players, num):
    q = Queue.from_iterable(players)
    while q.size() > 1:
        for _ in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


# print(play(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
import collections