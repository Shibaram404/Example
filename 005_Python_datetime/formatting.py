from datetime import *

def main():
    new = datetime.now()

    # date formatting
    print(new.strftime("The current year is %Y"))
    print(new.strftime("only date: %d, short day: %a, short month: %b, short year: %y"))
    print(new.strftime("full date: %D, full day: %A, full month: %B, full year: %Y"))
    print(new.strftime("Local date & time: %c"))
    print(new.strftime("Local date: %x"))
    print(new.strftime("Local time: %X"))

    # time formatting
    print(new.strftime("Current time: %I:%M:%S %p"))
    print(new.strftime("24-hour clock: %H:%M"))


if __name__ == "__main__":
    main();
