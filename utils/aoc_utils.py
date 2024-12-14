import re

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def subtract(a, b):
    return a[0] - b[0], a[1] - b[1]

def mult(a, scal):
    return a[0] * scal, a[1] * scal

def negate(a):
    return -a[0], -a[1]

def get_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))
