# find how many days a atom take to decay frpm it's initial to final
N = int(input("Enter your initial atom number: "))
R = int(input("Enter your final atom number: "))
count = 0
while N > R:
	N //= 2
	count += 1
print(count * 12)   # 12 days is the half life of base atom
