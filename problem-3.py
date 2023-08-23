#Problem 3
'''
Prime FActors
'''
n=600851475143
#n=13195
for i in range(2,n+1):
    if n%i==0:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break;
            
        if flag==0:
            my_list=[]
            my_list.append(i)
            print(my_list)

largest=max(my_list)
print('The Largest Prime Factor is: ',largest)