# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
array = list(map(int,input().split()))


a = list(map(int,input().split()))
b = list(map(int,input().split()))

happy = 0
for i in range(len(array)):
    if array[i] in a:
        happy+=1
    if array[i] in b:
        happy-=1
print(happy)
    
