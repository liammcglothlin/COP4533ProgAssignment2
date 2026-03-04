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

def simulate_lru(k, req):
    cache = OrderedDict()
    misses = 0

    for x in req:
        if x in cache:
            cache.move_to_end(x)  # hit -> most recent
        else:
            misses += 1
            if len(cache) == k:
                cache.popitem(last=False)  # evict least recent
            cache[x] = True

    return misses

def precompute_next_use(req):
    next_use = [INF] * len(req)
    next_pos = {}

    for i in range(len(req) - 1, -1, -1):
        x = req[i]
        next_use[i] = next_pos.get(x, INF)
        next_pos[x] = i

    return next_use


def simulate_optff(k, req):
    next_use = precompute_next_use(req)

    in_cache = set()
    item_next = {}
    misses = 0

    for i in range(len(req)):
        x = req[i]

        if x in in_cache:
            item_next[x] = next_use[i]
            continue

        misses += 1

        if len(in_cache) < k:
            in_cache.add(x)
            item_next[x] = next_use[i]
        else:
            victim = max(in_cache, key=lambda y: item_next[y])
            in_cache.remove(victim)
            del item_next[victim]

            in_cache.add(x)
            item_next[x] = next_use[i]

    return misses

def main():
    k, m, req = read_stdin()

    fifo = simulate_fifo(k, req)
    lru = simulate_lru(k, req)
    opt = simulate_optff(k, req)

    print("FIFO  :", fifo)
    print("LRU   :", lru)
    print("OPTFF :", opt)


if __name__ == "__main__":
    main()