# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    x = int(input())
    l = list(map(int,input().split()))
    state = True
    
    
    while len(l)>1:
        if l[0] >= l[-1]:
            max_num = l[0]
            l.pop(0)
        else:
            max_num = l[-1]
            l.pop(-1)
        if max_num < l[0] or max_num < l[-1]:
            state = False
            break
    print("Yes" if state else "No")
            
