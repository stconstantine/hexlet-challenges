# Just fibonacci numbers, using recursion
# https://ru.hexlet.io/challenges/python_basics_fib_exercise

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
