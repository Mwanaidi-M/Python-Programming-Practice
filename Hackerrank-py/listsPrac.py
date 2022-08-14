'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer i at position e.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types 
listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''

size = int(input('How many commands:\t'))

ls = []

for s in range(size):
    comm = input().split()

    com, val = comm[0], comm[1:]

    val = list(map(int, val))

    if com == 'insert':
        ls.insert(val[0], val[1])

    elif com == 'print':
        print(ls)

    elif com == 'remove':
        ls.remove(val[0])

    elif com == 'append':
        ls.append(val[0])

    elif com == 'pop':
        ls.pop()
    
    elif com == 'sort':
        ls.sort()

    elif com == 'reverse':
        ls.reverse()