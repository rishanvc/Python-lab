from mypackage import sum as s
from mypackage import avg as a
from mypackage import pow as p

n=int(input("enter the number 1\n"))
m=int(input("enter the number 2\n"))
print("sum = ",s.sum(n,m))
print("avg = ",a.avg(n,m))
print("pow = ",p.pow(n,m))
