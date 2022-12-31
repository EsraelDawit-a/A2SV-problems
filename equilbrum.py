xi,yi,yj = 0,0,0
for i in range(int(input())):
    x,y,j = map(int,input().split())
    xi+=x
    yi+=y
    yj+=j
print("YES" if (xi==yi==yj==0) else "NO")
