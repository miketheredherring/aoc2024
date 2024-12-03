#! /usr/bin/env python3
from collections import defaultdict

def parse_file(filename):
    l1 = []
    l2 = []
    with open(filename, 'r') as f:
        for line in f:
            vals = line.split(' ')
            l1.append(int(vals[0]))
            l2.append(int(vals[-1]))
    return l1, l2

def prepare_lists(l1, l2):
    l1.sort()
    l2.sort()
    return l1, l2

def process_lists(l1, l2):
    s = 0
    for v1, v2 in zip(l1, l2):
        s += abs(v1 - v2)
    return s

def process_lists_two(l1, l2):
    s = 0
    sl1 = {k for k in l1}
    for v in l2:
        if v in sl1:
            s += v
    return s

if __name__ == '__main__':
    l1, l2 = parse_file('input.txt')
    prepare_lists(l1, l2)
    ans = process_lists(l1, l2)
    ans_2 = process_lists_two(l1, l2)
    print(ans)
    print(ans_2)
