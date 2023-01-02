# Enter your code here. Read input from STDIN. Print output to STDOUT
container = []
for i in range(int(input())):
    container.append(input())
print(len(set(container)))
for item in set(container):
    print(container.count(item),end=" ")
