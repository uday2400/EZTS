a=[1,5,7]
# a.sort()
b=18
c=0
i=0
while b>0:
    if b>=a[i] and i<len(a):
        c+=1
        b=b-a[i]
        print(a[i],b,c)

    else:
        i+=1

print(c)

        
        

# print(a.sorted(reversed))