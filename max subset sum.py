from itertools import combinations
#set={1,2,3,4}
set=set(map(int,input("enter element with space wise").split()))
l=[]
l2=[]
for i in range(1,len(set)+1):
    comb=list(combinations(set,i))
    l.extend(comb)

for i in l:
    l2.append(sum(i))
print(f"max subset sum is={max(l2)}")  
