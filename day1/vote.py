vote=list(map(int, input("enter the number of votes:").split(" ")))
count=[0]*6
for i in vote:
    count[i-1]=count[i-1]+1
print(vote,count)
