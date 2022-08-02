#!/bin/python3

def countSwaps(a):

    array = a
    c = 0
    
    ''' First Cheack if it is already Sorted in Reverse Order 
        if it is it takes length of array to be sorted and the firs item will 
        be the last item in the array, and the last item will be the first item in the array,
        
        if it is already sorted no need to sort
        
    '''
    if sorted(array,reverse=True) == array:
        print(f"Array is sorted in {len(array)} swaps.")
        print(f"First Element: {array[-1]}")
        print(f"Last Element: {array[0]}")
        
    
    elif sorted(array) == array:
        print(f"Array is sorted in {c} swaps.")
        print(f"First Element: {array[0]}")
        print(f"Last Element: {array[-1]}")
    else:
        while sorted(array) != array:
            for i in range(1,len(array)):
                if array[i]<array[i-1]:
                    array[i],array[i-1] = array[i-1],array[i]
                    c+=1
        print(f"Array is sorted in {c} swaps.")
        print(f"First Element: {array[0]}")
        print(f"Last Element: {array[-1]}")
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
