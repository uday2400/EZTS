import os
with open("myfile.txt","wb") as f:
    eid=1
    name="bat"
    condition="good"
    s=f"{eid},{name},{condition}\n"
    f.write(s.encode())
    s=f"{eid},{name},{condition}\n"
    f.write(s.encode())
    f.close()
    
with open("myfile.txt","r") as f:
    s=f.read()
    print(s)
    f.close()
#     print(f.tell())
#     f.seek(-10,2)
#     f.write(b"#")
#     print(f.read().decode('utf-8'))
    