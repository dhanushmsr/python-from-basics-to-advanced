# #TO get run time user input for list

# a=int(input("enter the size of list that you want: "))
# l1=[]
# for i in range(a):
#     l1.append(int(input(f"enter value of index {i}: ")))
# print(l1)


# #Sum of the element in the list

# sum=0
# for i in l1:
#     sum=sum+i
# print(sum)

# #product of elemnt in the list

# product=1
# for i in l1:
#     product=product*i
# print(product)

# #sort the list without sort method in list

# for i in range(len(l1)):
#     for j in range(i + 1, len(l1)):
#         if l1[i] > l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
# print(l1)

# #TO find the biggest element in the list
# max=0
# for i in l1:
#     if i>max:
#         max=i
# print(max)
    

# #To get the second largest element in the list

# m=l1[0]
# temp=l1[0]
# for i in l1:
#     if i>m:
#         temp=max
#         max=i
#     elif m>i>temp:
#         temp=i        
# print(temp)

#Sum of any sequences is equal to the grand total
l = [1, 2, 7, 3, 3, 10, 7, 6, 8]
target = 13

for i in range(len(l)):
    total = 0
    for j in range(i, len(l)):
        total += l[j]
        if total == target:
            print(l[i:j+1])