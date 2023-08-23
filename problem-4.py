#PROBLEM -4 $
'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.
'''
#QUESTION:Find the difference between the sum of the squares of the first one hundred
#(100) natural numbers and the square of the sum ? ? ?
n=100
sum1=0 #1^2 + 2^2 + ... + n^
sum2=0 #(1 + 2 + ... + n)^2 = (n(n+1)/2)^2
sum1=(n*(n+1)*(2*n+1))/6
sum2=(n*(n+1)/2)**2
print(sum2-sum1)


    
    
    