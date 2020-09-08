def strangeListFunction(n):

    strangeList = []

    s = 0

    for i in range(0, n):

        strangeList.insert(0, i)

        s += i

    print("the sum of list:", s)

    return strangeList



print(strangeListFunction(5))
