#print_anti diagonals
def print_anti(mat,R,C):
    #printint the First Half
    ans = []
    for i in range(R+C-1):
        temp = []
        if R > i:
            r = i
            c = 0
            while r>=0 and c<C:
                temp.insert(0,mat[r][c])
                r-=1
                c+=1
            ans.append(temp)
        else:
            r = R-1
            c = i-r
            while r>=0 and c<C:
                temp.insert(0,mat[r][c])
                r-=1
                c+=1
            ans.append(temp)
            
    return ans
    
#R,C = map(int,input().split())
'''
mat = [ [1 ,2, 3, 4],
        [5 ,6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]
       ]

'''
mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]
       ]
       
#mat = [[int(input()) for i in range(C)] for j in range(R)]
ans = print_anti(mat,3,4)
for num in ans:
    print(*num)
