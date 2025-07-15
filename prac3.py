import logging.config
import time
from contextlib import contextmanager
import csv
import pandas as pd
import io
import sys
from collections import deque
from functools import lru_cache
import logging
"""
queue1 = deque()
queue1.append(22)
queue1.append(77)
queue1.popleft()
print(queue1)"""

# --------------------------------------------------------------------------------------
"""def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n - 1)


print(factorial(7))"""
# -----------------------------------------------------------------------------------
"""from collections import deque
undo_stack = deque()
redo_stack = deque()


def performance(action):
    undo_stack.append(action)
    redo_stack.clear()


def undo():
    if undo_stack:
        action = undo_stack.pop()
        redo_stack.append(action)
        print(redo_stack)


def redo():
    if redo_stack:
        action = redo_stack.pop()
        undo_stack.append(action)


split = str("Hello world from python").split()
for i in split:
    performance(i)
undo()
print(undo_stack)
redo()
print(undo_stack)
undo()
undo()
redo()"""
# using decoraters


"""def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time-start_time
        print(
            f"Function {func.__name__} Exceution time {execution_time: .5f} seconds")
        return result
    return wrapper



@timer
def my_function(a, b):
    time.sleep(1)
    return a+b


result = my_function(5, 6)
print(f"result {result}")"""

# generator


"""def read_file(filename):
    with open(filename, "r") as f:
        read = csv.reader(f)
        for i in read:
            yield i


for m in read_file("sample_data.csv"):
    print(m)"""

# generator


"""def read(filename):
    df = pd.read_csv(filename)
    for i in df:
        yield i


for m in read("sample_data.csv"):
    print(m)"""

# contextmanager

"""
@contextmanager
def suprees_stdout():
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = original_stdout


with suprees_stdout():
    print("this will not be printed")
print("this will be printed")"""
# fibannoci squence


"""def fibannoci_squence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


fib = fibannoci_squence()
for i in range(10):
    print(next(fib))"""

# decorater


"""@lru_cache(maxsize=None)
def fibannoci(n):
    if n < 2:
        return n
    else:
        return fibannoci(n-1) + fibannoci(n-2)


print(fibannoci(35))"""

# decorater


"""def logger(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename="example.log", level=logging.INFO)
        logging.info(
            f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Result {result}")
        return result
    return wrapper


@logger
def my_function(a, b):
    return a**b


print(my_function(5, 7, ))"""

# generator


def cube(n):
    for i in range(1, n+1):
        yield i**3


n = int(input("enter:"))
c = cube(n)
for i in c:
    print(i)
    time.sleep(2)
