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
import random
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

# generator1 w3 resources


"""def cube(n):
    for i in range(1, n+1):
        yield i**3


n = int(input("enter:"))
c = cube(n)
for i in c:
    print(i)
    time.sleep(2)"""
# generator2


"""def rand_num(n):
    while True:
        yield random.randint(1, n)


w = rand_num(9)
for i in range(5):
    print(next(w))
    time.sleep(1)"""
# generator3


"""def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_nums_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


# Create the generator object
primes = prime_nums_generator()

# Accept input from the user
n = int(input("Input the number of prime numbers you want to generate? "))

# Generate and print the first 10 prime numbers
print("First", n, "Prime numbers:")
for _ in range(n):
    print(next(primes))"""
# generator4

"""
def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


fibannnoci = fibo()
n = int(input("enter a number"))
for i in range(n):
    time.sleep(1)
    print(next(fibannnoci))"""
# meta pogramming

"""
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def reduce_health(self, by):
        health -= by
        print(f"{self.name} has a health of {self.health}")


def create_character(name, health, strength):
    return Character(name, health, strength)


def create_enemy(name, health, strength):
    return Character(name, health, strength)


def when(action_description, action_function):
    print(f"Action: {action_description}")
    action_function()


def hero_attack_goblin():
    goblin.reduce_health(by=hero.strength)


hero = create_character(name="Hero", health=100, strength=50)
goblin = create_enemy(name="Goblin", health=20, strength=10)
when("Hero attacks Goblin", hero_attack_goblin)"""
# decorator

"""
def positive_argument(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Arguments must be positive")
        return func(*args)
    return wrapper


@positive_argument
def calculate_area(length, breadth):
    area = length*breadth
    return area


print(calculate_area(3, 5))
print(calculate_area(3, 5))"""
# classes


def create_user_class(class_name, attributes):
    """Dynamically creates a user class with given attributes."""

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in attributes:
                setattr(self, attr, value)
            else:
                raise AttributeError(f"Invalid attribute: {attr}")
    class_attrs = {"__init__": __init__}
    for attr in attributes:
        class_attrs[attr] = None
    return type(class_name, (object,), class_attrs)


BasicUser = create_user_class("BasicUser", ["username", "email"])
PremiumUser = create_user_class(
    # Corrected line
    "PremiumUser", ["username", "email", "subscription_level"])

basic_user = BasicUser(username="Alice", email="alice@example.com")
premium_user = PremiumUser(
    username="Bob", email="bob@example.com", subscription_level="gold")

print(basic_user.username)  # Output: Alice
print(premium_user.subscription_level)  # Output: gold
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper
@timer
def sub(crop,yie,m_rate):
    time.sleep(1)
    if crop.lower() == "rice":
        p = (yie*m_rate)+100
        return f"the price is {p}"
    return "crop not found"
print(sub("rice", 1000, 50))  