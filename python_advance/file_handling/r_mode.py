with open(r'C:\Users\mdhan\Desktop\python_A\name.csv','r') as f:
    print(f.read())
    f.seek(0)
    print(f.readline(2))
    f.seek(0)
    print(f.readlines())
    print(f.readable())