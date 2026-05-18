if __name__=='__main__':
    lst=[10,20,30,[1,2,3],'py',True]
    print(lst)
    # indexing (to access the single elements in a sequences based on the index value may be postive or negative)
    print(lst[1]) #20
    print(lst[-3]) #[1,2,3]
    print(lst[-2]) #py

    # slicing (to access the multi elements or portions of elements in the sequences)

    print(lst[0:len(lst):1]) # slicing will be like variable[start:stop:step] default start value is 0 and default step is 1
    print(lst[1:2]) #only stop and step 
    print(lst[-1:-5:-1]) #[True, 'py', [1, 2, 3], 30] by negative indexing
    print(lst[:3:]) #[10, 20, 30] only stop value

    #can modify the element after initilization
    lst[2]=10 #list can have duplicates and it is a muttable data type which can be modified after declarations
    print(lst) #10, 20, 10, [1, 2, 3], 'py', True]

    #built in methods of list
    # append method to add single element at the end of the list
    lst.append(10) #add the elements at the last only one value can add at a time and return is none
    print(lst) #[10, 20, 10, [1, 2, 3], 'py', True, 10] appending list inside list also possible

    # extend() to add multiple value at the end of the list
    lst.extend([7,6,5,4])  #[10, 20, 10, [1, 2, 3], 'py', True, 10, 7, 6, 5, 4]                                                
    print(lst)              #add the give sequences in the existing list at the end
    
    l=['l','e','t','a']
    print(l.sort())

    # print the n natural number
    l=[]
    n=int(input("enter the number of natural numbers in list: "))
    for i in range  (n):
        l.append(i)
    print(l)

    # user input in list

    l=[]
    n=int(input("enter the size of List"))
    for i in range (n):
        l.append(int(input(f"enter the index[{i}] :")))
    print(l)