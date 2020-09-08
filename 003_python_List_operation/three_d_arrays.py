rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True  # book a room 
rooms[0][0][1] = True
rooms[0][4][1] = False   # release the second room on the fifth floor located in the first building
print(rooms)

# check the vacancies of room in 15th floor of the third building

vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1

print("vacacies in 15th floor of third building are: ", vacancy)
