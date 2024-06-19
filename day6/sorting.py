def sorting(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=[4,3,2,1,5,6,8]
sorting(a)
print(a)