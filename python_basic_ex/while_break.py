word = "chupacabra"
user = input("enter a word : ")
while word != user:
    user = input("enter a word : ")
    if user == word:
        break
print("You've successfully left the loop.")
