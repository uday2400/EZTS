# def ss(a):
#     n=len(a)
    
#     for j in range(0,n):
#             pos=j
#             min=a[j]
#             for i in range(0,n-1):
#                 if a[i]<min:
#                       min=a[i]
#                       pos=i
#                 a[i] ,a[pos] = a[pos],a[i]
# a=[4,3,2,1]
# ss(a)
# print(a)


def selection_sort(a):
      n=len(a)
      for i in range(n):
            min=i
            for j in range(i+1,n):
                  if a[j]<a[min]:
                        min=j
            a[i],a[min]=a[min],a[i]
            
a=[4,3,2,1]
selection_sort(a)
print(a)