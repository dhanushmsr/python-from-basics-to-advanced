with open(r'name.txt','x') as f:
    f.write("Hi i am good")
    f.seek(0)
    f.write("\tthe sun is yellow in colour")
    print(f.tell())
    f.seek(10)
    f.truncate()
    print(f.tell())