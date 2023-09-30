year=int(input("Enter the year"))
factorial=1
if(year%400==0)and(year%100==0):
    print(year," is leap year")
elif(year%4==0)and(year%100!=0):
    print(yea,r" is leap year")
else:
    print(year," is not leap year")
