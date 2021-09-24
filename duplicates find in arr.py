N=int(input("enter value of N : "))
l=[]
dupcount=0
for i in range(N+1):
    l.append(int(input(f"enter elements of position {i} : ")))
s=list(set(l))
for i in s:
    if l.count(i)!=1:
        dupcount+=1
        
print(f"{dupcount} elements are duplicates")