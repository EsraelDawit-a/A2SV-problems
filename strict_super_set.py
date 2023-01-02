# Enter your code here. Read input from STDIN. Print output to STDOUT HackerRank
super_sets = input().split()
flag = True
for i in range(int(input())):
    sub_sets = input().split()
    for sets in sub_sets:
        if sets not in  super_sets:
            flag = False
            break
        
print(flag)
    
