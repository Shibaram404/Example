beatles = []

print("Step 1:", beatles)


beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George_Harrison")


print("Step 2:", beatles)

n = 2
for i in range(0, n):
    ele = input("add the following members: ") 
    beatles.append(ele)

print("Step 3:", beatles)



del beatles[3 : 5]

print("Step 4:", beatles)



beatles.insert(0, "Ringo Starr")

print("Step 5:", beatles)





# testing list legth

print("The Fab", len(beatles))
