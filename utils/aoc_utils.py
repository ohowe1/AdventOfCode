import re

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def subtract(a, b):
    return a[0] - b[0], a[1] - b[1]

def mult(a, scal):
    return a[0] * scal, a[1] * scal

def negate(a):
    return -a[0], -a[1]

def mp_get(mp, tup):
    return mp[tup[0]][tup[1]]

def mp_set(mp, tup, set):
    mp[tup[0]][tup[1]] = set

def get_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))
