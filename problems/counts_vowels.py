def count_vowel(str):
    count=0
    for i in str:
        if i in "aAeEiIoOuU":
            count+=1
    return count
print(count_vowel(str(input("Enter the word"))))