# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

import re
import sys

def main():
    time = (validating_input(input("What time is it? ").strip()))
    if time:
        print(convert(time))
        print(eating_time(time)) 


def validating_input(time):
        if am_pm_format := re.search(r"^(0[1-9]|1[0-2]|[1-9]):([0-5][1-9]|[1-5][0-9]) (?P<meridiem>a.m.?|p.m.?|AM|PM)$", time):
            hour,minute,meridiem = am_pm_format.groups()
            if "AM" in meridiem or "a.m" in meridiem:
                hour = int(hour) + 12
            return str(hour),minute
        if date_format := re.search(r"^(\d?\d):([0-5]\d)$", time):
            hour,minute = date_format.groups()
            return hour, minute
        else:
            return False


def convert(time):
        hour, minute = time
        format_min = int(minute) / 6
        minutes = f"{format_min:.0f}"
        if minutes == "10":
             return f"{hour}.9" 
        else:
            return f"{hour}.{minutes}"


def eating_time(time):
        hour,minute = time
        check_time = hour + minute
        hour, minute = int(hour), int(minute)
        if 700 <= int(check_time) <= 800:
            return "Breakfast time" 
        elif 1200 <= int(check_time) <= 1300:
            return "Lunch time"
        elif 1800 <= int(check_time) <= 1900:
            return "Dinner time"
        else:
            sys.exit()


if __name__ == "__main__":
    main()