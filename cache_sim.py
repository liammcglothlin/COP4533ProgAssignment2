#!/usr/bin/env python3
import sys
from collections import deque, OrderedDict

INF = 10**18


def read_stdin():
    first_line = input().split()
    k = int(first_line[0])
    m = int(first_line[1])

    second_line = input().split()
    req = list(map(int, second_line))

    return k, m, req


def simulate_fifo(k, req):
    in_cache = set()
    q = deque()
    misses = 0

    for x in req:
        if x in in_cache:
            continue  # hit

        misses += 1  # miss

        if len(in_cache) < k:
            in_cache.add(x)
            q.append(x)
        else:
            victim = q.popleft()
            in_cache.remove(victim)

            in_cache.add(x)
            q.append(x)

    return misses




def main():
    k, m, req = read_stdin()

    fifo = simulate_fifo(k, req)
    

    print("FIFO  :", fifo)
    


if __name__ == "__main__":
    main()