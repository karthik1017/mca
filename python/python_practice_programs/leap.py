year = int(input("enter the value for leap year: "));
if(year % 4 == 0):
    if(year % 100 != 0):
        print("the year",year,"is a leap year");
    else: 
        print("the year",year,"is not a leap year");
else:
    print("the year",year,"is not a leap year");


