arr=list(map(int,input("enter element with spacewise").split()))
temp=[]
for i in arr:
    if i<0:
        arr.remove(i)
        temp.append(i)
print(arr+temp)
