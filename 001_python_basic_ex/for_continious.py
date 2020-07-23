# vowel eater

wordWithoutVowels = ""
# Prompt the user to enter a word
userWord = input("enter a word : ")
userWord = userWord.upper()
# and assign it to the userWord variable.
for letter in userWord:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordWithoutVowels += letter
print(wordWithoutVowels)
