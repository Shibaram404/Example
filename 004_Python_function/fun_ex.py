def msg():
    print("Enter the number: ")

msg()
print("1 - '+'\n","2 - '**'\n","3 - '*'\n","4 - '/'")

j = int(input())


if j == 1:
    a = 0
    b = 0
    while a < 10:
        msg()
        ab = int(input())
        b += ab
        a += 1
        print(b)

    print("the final sum of all input is :", b)

elif j == 2:
    a = 0
    b = 0
    while a < 10:
        msg()
        ab = int(input())
        ab = ab ** 2
        a += 1
        print(ab)
        b += ab

    print("the final addition of all square input  is :", b)

elif j == 3:
    a = 0
    b = 1
    while a < 10:
        msg()
        ab = int(input())
        b *= ab
        a += 1
        print(b)

    print("the final sum of all input is :", b)
