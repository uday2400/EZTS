def calc_max(p,w,c,n):
    if n==0 or c==0:
        return 0
    if DP[n][c]!=-1:
        return DP[n][c]
    if (w[n-1]<=c):
        DP[n][c]=max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))
        return DP[n][c]
    else:
        DP[n][c]=calc_max(p,w,c,n-1)
        return DP[n][c]
   
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
c=15
n=len(p)
DP=[[-1 for i in range(c+1)] for j in range(n+1)]

print(calc_max(p,w,c,n))
print(DP)