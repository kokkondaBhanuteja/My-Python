limit=1000
for a in range(1,limit//3):
    for b in range(2,limit//2):
        c=limit-b-a
        if((a*a + b*b)==(c*c)):
            print(a,'\t',b,'\t',c)
            product=a*b*c
            print("The Pythagorean Triplet is :",product)
            
            
        
