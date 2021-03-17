#!/usr/bin/env python3.7

def inspect(func, *args):
    print(f"Running {func.__name__}")
    val = func(*args)
    print(val)
    return val

def combine(a, b):
    return a + b
