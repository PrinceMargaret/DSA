arr1=list(map(int, input("enter element wit spacewise A=: ").split()))
arr2=list(map(int, input("enter element wit spacewise B=: ").split()))
arr1.sort()
arr2.sort()
A,B=set(arr1),set(arr2)
print(f"A U B ={A|B} \n A intesection B {A & B}")
