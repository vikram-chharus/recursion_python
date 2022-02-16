import sys
from trace_recursion import trace 
sys.path.append("..")

def factorial(n):
    if n<=1:
        #base case
        return 1
    else:
        return n* factorial(n-1)

factorial = trace(factorial)
print(factorial(5))