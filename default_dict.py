# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
word_map = defaultdict(list)
n,m = map(int,input().split())
for i in range(n):
    value = input()
    word_map[value].append(str(i+1))
for j in range(m):
    val = input()
    if val in word_map:
        print(" ".join(word_map[val]))
    else:
        print(-1)
