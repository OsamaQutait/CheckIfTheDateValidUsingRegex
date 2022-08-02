import re
from DateFile import *
def isValidDate(date):
    month_and_day = {1: 31,
                     2: 28,
                     3: 31,
                     4: 30,
                     5: 31,
                     6: 30,
                     7: 31,
                     8: 31,
                     9: 30,
                     10: 31,
                     11: 30,
                     12: 31}
    leapYearFalg = False
    validDateFlag = False
    result = re.findall("(\d{4})(\.|\-)(0[1-9]|1[0-2])(\.|\-)([1-2]\d|0[1-9]|3[0-1])", date)
    date = Date(int(result[0][0]), int(result[0][2]), int(result[0][4]))
    if result:
        if date.getYear() % 100 == "00":
            if date.getYear() % 4 == 0:
                leapYearFalg = True
            else:
                leapYearFalg = False
        else:
            if date.getYear() % 400 == 0:
                leapYearFalg = True
                #print("Leap year ^_^")
            else:
                leapYearFalg = False
                #print("Not Leap year")
        if leapYearFalg:
            if date.getMonth() == 2:
                if date.getDay() <= 29:
                    validDateFlag = True
                else:
                    validDateFlag = False
            elif month_and_day[date.getMonth()] >= date.getDay():
                validDateFlag = True
            else:
                validDateFlag = False
        else:
            if month_and_day[date.getMonth()] >= date.getDay():
                validDateFlag = True
            else:
                validDateFlag = False
        #print("the date is valid")
    else:
        print("the date is invalid")
    if leapYearFalg and validDateFlag:
        print("Leap year and the date is valid ^_^")
    else:
        print("the date is invalid")

if __name__ == '__main__':
    isValidDate("2001.02.29")

