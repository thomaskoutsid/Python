'''
Thomas Koutsidis
June 16th, 2022

Question 3

The function in_date() prompts the user for a month, day and year.
It returns a list of [month, day, year] assuming the user enters a string for month and integers for day and year.
The function is_month(month) returns True if month is a valid month and False otherwise.
The function is_day(month, day) returns True if the day is a valid day in month and False otherwise.
The function is_leap_year(year) returns True is year is a leap year and False otherwise.
The main() function uses the in_date() function to get a date as alist and calls the other three functions to determine if it is a valid date in a leap year.
'''

def in_date():
    month = input("Enter a month: ")
    day = int(input("Enter a day: "))
    year = int(input("Enter a year: "))
    return [month, day, year]


def is_month(month):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    valid_month = False
    for m in months:
        if month == m:
            valid_month = True
            break
    return valid_month


def is_day(month, day):
    for month in ["January", "March", "May", "July", "August", "October", "December"]:
        if day <= 31:
            return True
        else:
            return False
    for month in ["February"]:
        if day <= 28:
            return True
        else:
           return False
    for month in ["April", "June", "September", "November"]:
        if day <= 30:
            return True
        else: 
            return False


def is_leap_year(year):
    if year % 400 == 0:
        return "This is a valid date in a leap year!"
    elif (year % 4 == 0) and (year % 100 != 0):
        return "This is a valid date in a leap year!"
    else:
        return "This is not a valid date in a leap year."

def main():
    print("This program determines a valid date in a leap year.")
    date = in_date()
    month = date[0]
    check_month = is_month(month)
    if check_month == False:
        print("This is not a valid month.")
        return
    day = date[1]
    check_day = is_day(month, day)
    if check_day == False:
        print("This is not a valid day in the month.")
    year = date[2]
    if (year < 1) or (year > 2022):
        print("Error. This is not a valid year.")
    leap_year = is_leap_year(year)
    if leap_year == True:
        if month in ["February"]:
            day <= 29
            return True
    print(leap_year)
    
    
main()   
