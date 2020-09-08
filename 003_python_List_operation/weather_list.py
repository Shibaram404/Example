noon1 = 30.5 # we can put more values for experiment
noon2 = 35.5
temps = [[0.0 for h in range(24)] for d in range(31)]
temps[1][11] = noon1
temps[0][11] = noon2
print(temps)

# avg. temp. of noon..................................................................
total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

## the highest temperature during the whole month..........................................
highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

### count the days when the temperature at noon was at least 20 ℃...........................
hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")
