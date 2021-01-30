inputYear = int(input("Input a year: "))

if(inputYear % 4 == 0):
    if(inputYear % 100 == 0):
        if(inputYear % 400 == 0):
            print(str(inputYear) + " is a leap year")
        else:
            print(str(inputYear) + " is not a leap year")
    else:
        print(str(inputYear) + " is a leap year")
else:
    print(str(inputYear) + " is not a leap year")