import re

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def subtract(a, b):
    return a[0] - b[0], a[1] - b[1]

def mult(a, scal):
    return a[0] * scal, a[1] * scal

def negate(a):
    return -a[0], -a[1]

def mpget(mp, tup):
    return mp[tup[0]][tup[1]]

def mpset(mp, tup, set):
    mp[tup[0]][tup[1]] = set

def mplen(mp):
    return len(mp), len(mp[0])

def get_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))

def make_2d(val, n, m):
    return [[val for a in range(m)] for b in range(n)]
