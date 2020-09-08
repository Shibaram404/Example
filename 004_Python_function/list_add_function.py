def list_sum(lst):

    s = 0

    for i in lst:

        s += i

    return s


lst = []



a = int(input("Enter the 1st number of list: "))

b = int(input("Enter the 2nd number of list: "))

c = int(input("Enter the 3rd number of list: "))

lst.append(a)

lst.append(b)

lst.append(c)


print("The list is:",lst)

print("the sum of the list is:", list_sum(lst))
