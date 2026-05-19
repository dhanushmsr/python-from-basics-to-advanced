# w+ “Open for read/write, but first delete everything inside the file.”
# r+ keeps existing content ,allows reading and writing, does not erase the file
with open ("name.txt","w") as w:
    w.write("this is hellow world")