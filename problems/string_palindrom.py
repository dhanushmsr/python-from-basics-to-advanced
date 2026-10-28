def str_palindrom(str):
    left=0
    right=len(str)-1

    while left<right:
        if str[left]==str[right]:
            left=left+1
            right=right-1
        else:
            return False

    return True

print(str_palindrom("madam"))
print(str_palindrom("malayayalam"))
print(str_palindrom("dhanush"))
