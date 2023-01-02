# Enter your code here. Read input from STDIN. Print output to STDOUT

hash_map = {}
k = int(input())
rooms = list(map(int,input().split()))
for room in rooms:
    hash_map[room] = hash_map.get(room,0)+1
    
for item in hash_map.keys():
    if hash_map[item] < k:
        print(item)
        break
