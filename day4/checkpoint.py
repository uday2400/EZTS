#sum of left and right are equal it will return index of the number where the chckpoint is

a=[4,3,5,1,1,1,1,1,3,6]
# c=int(input())
for i in range(len(a)):
    
#     i=c
    left=a[:i]
    right=a[i:]
#     print(left,right)
    suml=sum(left)
    sumr=sum(right)
#     print(suml,sumr)
    if suml==sumr:
        
        print("checkpoint=",i)
        break
    else:
#         i=i+1
#         print(c)
        continue
              
# print(left,right)
# print(suml,sumr)
# print("checkpoint=",a.index(a[c])
    
    