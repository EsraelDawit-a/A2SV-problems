#!/bin/python3

# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    num = arr[-1]
    narr = [item for item in arr]
    i = n-1
    while sorted(arr)!=narr:
        if i>0:
            if narr[i-1]>num:
                narr[i] = narr[i-1]
                print(*narr)
                
                i-=1
            else:
                narr[i] = num
                print(*narr)
                break

        else:
            narr = sorted(arr)
            print(*sorted(arr))
       
           
 
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
