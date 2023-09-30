num1=int(input("enter the start year"))
num2=int(input("enter the end year"))
for year in range(num1,num2):
    if((year%4==0)and(year%100!=0)|(year%400==0)):
       print(year)
    
       
