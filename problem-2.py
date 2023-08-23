a=0
b=1
c=0
sum=0
i=1
for i in range(4000000):
    c=a+b
    a=b
    b=c
    if (c%2==0 and c<4000000):
        sum+=c
    
print(sum)


