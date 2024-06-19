#code

class Std:
    def __init__(self):
        self.usn=None
        self.name=None
        self.marks=[]
        self.a=None
#         self.grade=None
        
    def mark(self):
        
        self.name=input("Enter the name of the Student:")
        
        self.usn=input("Enter the usn:")
        
        print("Enter the marks of 5 subjects:")
        for i in range(1,6):   
            print(f"subject[{i}]:",end=" ")
            m=int(input())
            self.marks.append(m)
    
    
    def details(self):
#         print("Details of the student:")
        b=[self.usn,self.name,self.marks,self.a,self.grade]
        return b
    
    def per(self):
        n=sum(self.marks)
        self.a=(n/500)*100
#         print(self.a)
        
        
    def grade(self):
        if  85<=self.a<=100:
            self.grade="A"
        elif 60<=self.a<85:
            self.grade="B"
        elif 35<=self.a<60:
            self.grade="C"
        else:
            self.grade="fail"
            
    def covert_ob(self,stu_list):
        self.usn = stu_list[0]
        self.name = stu_list[1]
        self.marks = stu_list[2]
        self.a = stu_list[3]
        self.grade = stu_list[4]
        
    def print_details(self):
        print("Name: ",self.name)
        print("USN : ",self.usn)
        print("Marks in Five Subject are :")
        for i in range(0,5):
            print(f"Subject {i+1} = {self.marks[i]}")
        print("Percentage : ", self.a)
        print("Grade : ", self.grade)
            
s=Std()
s.mark()

s.per()
s.grade()
s.details()
s.print_details()
        



print()       
print()       
print()       
print()       
print()       
with open("u.txt","ab") as File:
    L=s.details()
    data = f"{L[0]}|{L[1]}|{L[2][0]},{L[2][1]},{L[2][2]},{L[2][3]},{L[2][4]}|{L[3]}|{L[4]}"
    File.write(data.encode())
    File.close()       
    u=[]

with open("u.txt",'rb') as File:
    data = File.readline().decode('utf-8')
    print(data)
    for i in data.split("|"):
        u.append(i)
#     print(stu_list)
    mrks=u[2]
#     print(mrks)
    mrks_list =[]
    for i in mrks.split(','):
        mrks_list.append(i)
#     print(mrks_list)
    u[2]=mrks_list


print(u)
c=Std()
c.covert_ob(u)
c.details()
c.print_details()
    