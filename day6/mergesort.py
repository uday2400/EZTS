def merge(l):
   if len(l)>1:
    mid=len(l)//2
    left=l[:mid]
    right=l[mid:]
    merge(left)
    merge(right)
    print(left,right)
    i=j=k=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l[k]=left[i]
            i+=1
            k+=1
        else:
            l[k]=right[j]
            j+=1
            k+=1

    while i<len(left):

        l[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        
        l[k]=right[j]
        j+=1
        k+=1   


a=[3,2,4,5,1]
merge(a)    
print(a)
