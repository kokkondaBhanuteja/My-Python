#CHecking Prime or NOT
def check_prime(my_input):
    for a in range(2,my_input):
        if(my_input%a==0):
            return False
            break
    return True

#function   
def Nth_prime(my_input):
    start=3
    i=2
    if(my_input==1):
        return 2
    else:
        while(i<my_input):
            start+=2
            if check_prime(start):
                i+=1
    return start    

#INPUT HERE!!
n=int(input('Enter a Nth Value of Prime Number:\n'))
print('The',n,'th Value prime is: ',Nth_prime(n))
