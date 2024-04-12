#Kth bit is set or not
def find(n,k):
    k-=1
    n  = n>>k
    if(n&1):
        return True
    return False
n = int(input("ENter a number: "))
k = int(input("Enter the bit size: "))
print(find(n,k))