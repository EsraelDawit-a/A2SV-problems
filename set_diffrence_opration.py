# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_num = int(input())
eng = set(map(int,input().split()))
fre_num = int(input())
fre = set(map(int,input().split()))

print(len(eng.difference(fre)))
