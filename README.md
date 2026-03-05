Programming Assignment 2: Greedy Algorithms

COP4533 – Spring 2026

Student Information

Name: Liam C. McGlothlin
UFID: (20475544)

This project implements and compares three cache eviction policies:

FIFO (First-In, First-Out)

LRU (Least Recently Used)

OPTFF (Belady’s Farthest-in-Future)

The program simulates how a cache behaves when processing a sequence of requests.
If the requested item is already in the cache, it is a cache hit.
If it is not present, it is a cache miss.

When a miss occurs:

If the cache is not full, the item is inserted.

If the cache is full, one item must be evicted according to the policy.

The program counts and reports the number of misses for each eviction policy.


Source Code

The implementation is contained in:

cache_sim.py

The program simulates the three eviction policies and prints the number of cache misses.



Build / Compilation Instructions

No compilation is required. The program is written in Python.

Requirements:

Python 3.x

Run Instructions

Run the program using Python:

python3 cache_sim.py

The program reads input from standard input.

Input format:

k m
r1 r2 r3 ... rm

Where:

k = cache capacity

m = number of requests

r1...rm = request sequence

Example

Example input:

3 10
1 2 3 4 1 2 5 1 2 3

Example output:

FIFO  : 8
LRU   : 8
OPTFF : 6
Assumptions

Cache capacity 
k≥1.

Requests are integers representing item IDs.

Input sequences contain exactly m requests.

The program processes requests in the order provided.


Answers to questions can be found in pgassignment2.pdf
