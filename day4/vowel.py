
def cv(p1):
    
    d={"a":0,"e":0,"i":0,"o":0,"u":0,}

    for i in range(len(p1)):

        if p1[i]=="a" or p1[i]=="A" :
            d["a"]+=1
            continue
        elif p1[i]=="i" or p1[i]=="I":

            d["i"]+=1

            continue

        elif p1[i]=="e" or p1[i]=="E":

            d["e"]+=1

            continue

        elif p1[i]=="o" or p1[i]=="O":

            d["o"]+=1

            continue

        elif p1[i]=="u" or p1[i]=="U" :

            d["u"]+=1

            continue
    q=max(d.values())
    r=[]
    for i,j in d.items():
        if j==q:
            r.append(i)
    return r


# # p1=input()
# p1="I am uday"
# p2="Today is Saturday"
# p3="aaa"
# p4="uhfaushfiii"
# print("p1=",p1[:])
# # c1=0
# # c2=0
# # c3=0
# # c4=0
# # c5=0
def cv(p1):
    
    d={"a":0,"e":0,"i":0,"o":0,"u":0,}

    for i in range(len(p1)):

        if p1[i]=="a" or p1[i]=="A" :

    #         print(p1[i])
            d["a"]+=1
            continue
        elif p1[i]=="i" or p1[i]=="I":
    #         print(p1[i])
    #         c2=c2+1
            d["i"]+=1

            continue

        elif p1[i]=="e" or p1[i]=="E":
    #         print(p1[i])
    #         c3=c3+1
            d["e"]+=1

            continue

        elif p1[i]=="o" or p1[i]=="O":
            
    #         print(p1[i])
    #         c4=c4+1
            d["o"]+=1

            continue

        elif p1[i]=="u" or p1[i]=="U" :
    #         print(p1[i])
    #         c5=c5+1
            d["u"]+=1

            continue
    # print("a=",c1)
    # print("e=",c3)
    # print("i=",c2)
    # print("o=",c4)
    # print("u=",c5)

#     print(d)
    q=max(d.values())
#     print(q)
    r=[]
    for i,j in d.items():
        if j==q:
            r.append(i)
    return r

p=[
    ["uday","hello"],
    ["charan","Hii"],
    ["vishwa","Hey"],
    ["srinivas","Bye"]
]

d1={}

for i in p:
    d1[i[0]]=cv(i[1])
    
print(d1)