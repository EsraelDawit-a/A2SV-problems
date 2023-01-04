#!/bin/python3
def if_else(n):
    if n%2!=0:
        return "Weird"
    elif (n%2==0 and n>=2 and n<=5):
        return "Not Weird"
    elif (n%2==0 and n>=6 and n<=20):
        return "Weird"
    else:
        return "Not Weird"
    


if __name__ == '__main__':
    n = int(input().strip())
    print(if_else(n))
