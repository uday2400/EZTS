def knapsack(we, val, W):
    n = len(we)
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w]=0
            elif we[i-1]<=w:
                K[i][w]=max(val[i-1]+K[i-1][w-we[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]

    
    return K[n][W]


w = [10,20,30]
v = [60,100,120]
c = 50
print(knapsack(w,v,c))