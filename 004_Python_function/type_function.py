def isInt(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(isInt(5))
print(isInt(5.0))
print(isInt("5"))
