# seek and tell
with open ("myfile.txt","r") as f:
    print(type(f))
    print(f.tell())
    print(len(f.read()))
    f.seek(10)
    
#     f.write("#")
#     print(f.read().decode('utf-8'))
    f.close()