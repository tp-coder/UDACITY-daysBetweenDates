# This is class 12 on 2nd module - Solving Problems
# Problem 1: given your birthday and the current date, calculate your age in days. Compensate for leap days. Assume that the birthday and corrent day are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 you are one day old.

def isLeapYear (year):
    '''
    This function tests whether a year is Leap, meaning February will have 29 days.
    If the year entered is divisible by 4, or is centurial and divisible by 400, it is a lead year.
    '''
    if isCenturialYear(year) == True:
        if (year % 400) == 0:
            return True
        else:
            return False
    if (year % 4) == 0:
        return True
    return False

def isCenturialYear(year):
    ''' This function tests whether an year is centurial, meaning is divisible by 100 '''
    if (year % 100) == 0:
        return True
    return False

def nextDay(year, month, day):
    """Function now accounts for correct number of days in each month"""
    stub_var = daysInMonth(year,month)
    if day >= stub_var:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        day += 1
    return (year, month, day)    

def daysBetweenDates(year1,month1,day1,year2,month2, day2):
    ''' This is the function that calculates que number of days between dates. '''
    days = 0
    date = (year1,month1,day1)
    final_date = (year2,month2,day2)
    if dateIsBefore(year1,month1,day1,year2,month2, day2) == True:
        while date != final_date:
            days += 1
            date = nextDay(*date)
    else:
        assert (dateIsBefore(year1,month1,day1,year2,month2, day2))
    return days

def daysInMonth(year, month):
    ''' This function returns the correct number of days a month has, be it leap or not. '''
    if isLeapYear(year) == True:
        day_of_months_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
        daysInMonth = day_of_months_leap[month-1]
        return daysInMonth
    else:
        day_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
        daysInMonth = day_of_months[month-1]
        return daysInMonth

def dateIsBefore(year1,month1,day1,year2,month2, day2):
    ''' This is a safe programming function that will test whether the current date comes before the searched date. '''
    if year1 > year2:
        return False
    if year1 == year2 and month1 > month2:
        return False
    if year1 == year2 and month1 == month2 and day1 > day2:
        return False
    return True

def test():
    ''' A few tests to check whether the code is correct =D. '''
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((1600,1,1,2017,12,31), 152671)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()