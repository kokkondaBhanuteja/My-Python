'''
ul=upperlimit   (&)
lm= Lower limit
'''
def LargestProduct(n):
    max_product=0 #intitializing maximum Product = 0
    ul = (10**(n))-1
    lm = (1+ul)//10
    for i in range(ul,lm-1,-1):
        for j in range(i,lm-1,-1):
            product=i*j
            if(product < max_product):
                break
            number=product
            rev=0
            while(number!=0):
                rem=number%10
                rev=rev*10+rem
                number//=10
                
            if (product==rev and product>max_product):
                max_product=product
    return max_product
    
#THe MAin Programm
n=int(input("Enter the Range : "))
result=LargestProduct(n)
print('The LArgest Palindrome PRoduct is = ',result)

