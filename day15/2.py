s="ABABABCANFKABABCNKABABCACNDA"
p="ABABCA"
# if p in s:
#     a=s.index(p)
# print(a)
l=[]
j=0
for i in range(len(s)):
    # for j in range(len(p)):
    if s[i]==s[j]:
        l.append(j+1)
        j+=1
    else:
        j=0
        l.append(j)
print(l)