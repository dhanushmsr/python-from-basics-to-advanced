with open('name.txt','w') as f:
    print(f.tell())
    # f.read()
    f.write("python")
    f.writelines(['python ',"1\t",'programming language'])
    f.seek(0)
    print(f.writable())