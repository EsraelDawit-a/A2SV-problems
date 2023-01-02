# Enter your code here. Read input from STDIN. Print output to STDOUT
# time limit exeeded
container = []
for i in range(int(input())):
    container.append(input())
print(len(set(container)))
for item in set(container):
    print(container.count(item),end=" ")



# more Faster solution using hashmap O(n+n) = > O(n)

# Enter your code here. Read input from STDIN. Print output to STDOUT
hash_map = {}
for i in range(int(input())):
    item = input()
    hash_map[item] = hash_map.get(item,0)+1
print(len(hash_map))
for key in hash_map.keys():
    print(hash_map[key],end =" ")
    
        
