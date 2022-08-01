import re
def isValidDate(date):
    result = re.findall("(\d{4})\.(0[1-9]|1[0-2])\.([1-2]\d|0[1-9]|3[0-1])", date)
    if result:
        if int(result[0][0]) % 100 == "00":
            if int(result[0][0]) % 4 == 0:
                print("Leap year ^_^")
            else:
                print("Not Leap year")
        else:
            if int(result[0][0]) % 400 == 0:
                print("Leap year ^_^")
            else:
                print("Not Leap year")
        print("the date is valid")
    else:
        print("the date is invalid")

if __name__ == '__main__':
    isValidDate("2000.07.31")

