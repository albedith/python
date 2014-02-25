'''
Created on Feb 21, 2014

@author: albedith
'''
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days_this_year = ((month2 - 1)*30.4167)+day2
    if (month2 < month1):
        years_alive = year2 - year1 - 1
    else:
        years_alive = year2 - year1
    leap_years = years_alive/4
    days_alive_no_leap = (years_alive - leap_years)*365
    days_alive_leap = leap_years*366
    total_days_alive = days_alive_no_leap+days_alive_leap+days_this_year
    print "                                      "
    print "total_days_alive= ",total_days_alive,"days_this_year= ",days_this_year,"years_alive= ",years_alive,"leap_years",leap_years
    print "                                      "
    return total_days_alive


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
