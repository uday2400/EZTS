##Greedy Algorithm
price=list(map(float,input().split()))
weight=list(map(float,input().split()))
profit=0
ratio_list=[]
max_weight=int(input())
for i in range(len(price)):
    ratio_list.append(price[i]/weight[i])
while max_weight>0:
    index=ratio_list.index(max(ratio_list))
    max_weight-=weight[index]
    profit+=price[index]
    ratio_list.pop(index)
    price.pop(index)
    weight.pop(index)

print(profit)
          