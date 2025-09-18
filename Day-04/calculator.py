import os
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

def add():
    return num1+num2

add_result = add()

def mul():
    return num1*num2

mul_result=mul()

if __name__ == '__main__':
    print(add_result)
    print(mul_result)