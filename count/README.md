# Python Projects: Countdown Timer 🐍

This repo contains a python code that generates a timer

```
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}" .format(mins, secs)
        print(timer)
        time.sleep = (0)
        t-=1
    print("timer completed")

t = input("Enter time in seconds: ")

print("\n")

countdown(int(t))
```

# CONCEPT DEFINITION

- `time module`: A python module that handles time related tasks

- `divmod`:  The divmod () is part of python’s standard library which takes two numbers as <br> parameters and gives the quotient and remainder of their division as a tuple. It is useful in many mathematical applications like checking for divisibility of numbers and establishing if a number is prime or not.

# CODE EXPLANATION

We start by importing the time module. Then we define a countdown function that divides time with the seconds using `divmod` function.
