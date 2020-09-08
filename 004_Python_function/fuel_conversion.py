# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def l100kmtompg(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def mpgtol100km(miles):
    km = miles * 1.609344
    gallon = 100 / km
    lit = gallon * 3.785411784
    return lit

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
