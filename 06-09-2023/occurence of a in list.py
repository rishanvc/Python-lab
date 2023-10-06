list=["rishan ","farook","binshad","shams"]
count=0
a='a'
print(list)
for i in list:
    for f in i:
        if(f==a):
            count=count+1
print("the number of ",a," in ",list," is ",count)
