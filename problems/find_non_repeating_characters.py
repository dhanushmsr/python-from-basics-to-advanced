def first_non_repeating_character(s):
    n=s.__len__()
    for i in range(n):
        found=False
        for j in range(n):
            if i!=j and s[i]==s[j]:
                found=True
                break
        if not found:
            return s[i]

print(first_non_repeating_character(input("enter word: ")))