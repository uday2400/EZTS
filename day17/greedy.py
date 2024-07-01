a=[[1,2,2,3],[3,1,4,2],[1,5,3,3],[1,2,1,1]]
# print(a[1][0])                                                                
'''
         _0_1_2_3
      0 | 1 2 2 3
      1 | 3 1 4 2
      2 | 1 5 3 3
      3 | 1 2 1 1


'''
n=len(a)
# print(n)
sum=a[0][0]


m=len(a[0])

i=0
j=0

while (i<n-1 or j<m-1):
    if i==len(a)-1:
        j+=1
    elif j==len(a)-1:
        i+=1
    
    elif a[i][j+1]<a[i+1][j]:
        # j=j+1
        # print(a[i][j+1])
        # print(a[i][j])
        # sum+=a[i][j]
        j=j+1
    else:
        # i=i+1
        # print(a[i+1][j])
        # print(a[i][j])

        # sum+=a[i][j]
        i=i+1
    sum+=a[i][j]

print(sum)
# for i in range(len(a)):
#     for j in range(len(a)):