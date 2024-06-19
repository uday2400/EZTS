from stack import Stack

e="[(())"
s=Stack()
ob="[{("
cb="]})"
flag=0
for i in e:
    if i in ob:
        s.push(i)
    if i in cb:
        x=s.pop()
        if x == "(" and i ==")":
            pass
        elif x == "{" and i =="}":
            pass
        elif x == "[" and i =="]":
            pass
        else:
            flag=1
            break
            
if (flag==0 ):
    print("valid")
else:
    print("invaid")