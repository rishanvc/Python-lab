a=[]
b=[]
n1=int(input("enter the size of the first list : "))
print("enter the elements of the first list ")
for i in range(0,n1):
    c=int(input(""))
    a.append(c)
n2=int(input("enter the size of the srcond list : "))
print("enter the elements of the second list ")
for i in range(0,n2):
    d=int(input(""))
    b.append(d)
suma=(sum(a))
aumb=(sum(b))
if suma==sumb:
    print("equal")
else:
    print("not equal")
