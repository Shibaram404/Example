length = 5
width = 10
height = 15
print(4 * (length + width + height))
print(2 * ((length*width) + (width*height) + (height*length)))
print(length * width * height )


# new
h = int(input())
w = int(input())
l = int(input())
allowed = (h <= 10 < w <= 35 < l <= 40) or (h + w + l <= 80)
print(allowed)

# next

dividend = int(input())
divider = int(input())
sol = (dividend % divider) == 0
print(sol)

#next
from datetime import date,datetime
birtday = datetime(year=2021, month=2, day=5)
countdown = birtday - datetime.now()
print(countdown)

#  flask ::ignore this::

from flask import *
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    # main algo
    birtday = datetime(year=2021, month=1, day=8)
    countdown = birtday - datetime.now()
    return "<h1>hello world<h1>"

if __name__ == "__main__":
    app.run()













