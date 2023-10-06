a=[]
n=int(input("enter leght of list : "))
print("enter the elements")
for i in range(0,n):
    ele=int(input(""))
    if ele > 100:
        a.append("over")
    else:
            a.append(ele)
print(a)

