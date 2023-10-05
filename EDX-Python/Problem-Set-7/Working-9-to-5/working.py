# Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

# Conversion Table
# In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# import re
# import sys


# def main():
#     print(convert(input("Hours: ")))


# def convert(s):
#     ...


# ...


# if __name__ == "__main__":
#     main()
# Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_working.py

import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if time := re.search(r"^((?:\d|1[0-2]?)(?:\:[0-5]\d)?) (?P<first_period>AM|PM) to ((?:\d|1[0-2]?)(?:\:[0-5]\d)?) (?P<second_period>AM|PM)$", s, re.IGNORECASE):
        print(time.groups())
        first_time = time_formats_handler(time.groups()[0], time.group("first_period"))
        second_time = time_formats_handler(time.groups()[2], time.group("second_period"))
        return f"{first_time} to {second_time}"
    else:
        raise ValueError



def time_formats_handler(time, period):
    try:
        if ":" not in time:
            hours = time
            minutes = "00"
        else:
            hours,minutes = time.split(":")
        if period.upper() == "AM":
            return f"{hours}:{minutes}"
        else:
            return f"{str(int(hours) + 12)}:{minutes}"
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    main()
