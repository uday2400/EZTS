#Prime Number
def prime(n):
    #n=int(input("Enter the number:"))
    f=0
    if n==0 or n==1:
        f=0

    for i in range(2,int(n/2)+1):

        if n%i == 0:
            f=1
            break
    if f==0:
        print("PN")
    else:
        print("not PN")
prime(0)