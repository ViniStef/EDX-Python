# Assuming there are 365 days in a year, there are 
#  minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour). But how many minutes are there in two or more years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them could have 
#  additional minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since! There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead. Fortunately, Python comes with a datetime module that has a class called date that can help, per docs.python.org/3/library/datetime.html#date-objects.

# In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD birth and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

# Structure your program per the below, not only with a main function but also with one or more other functions as well:

# from datetime import date


# def main():
#     ...


# ...


# if __name__ == "__main__":
#     main()
# You’re welcome to import other (built-in) libraries, or any that are specified in the below hints. Exit via sys.exit if the user does not input a date in YYYY-MM-DD birth. Ensure that your program will not raise any exceptions.

# Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more functions that test your implementation of any functions besides main in seasons.py thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

from datetime import date, timedelta,datetime
import re
import sys
import inflect

def main():
    birth_date = input("Date of Birth: ").strip()
    # formatted_date = handle_date(birth_date)
    # converted_date = convert_date(formatted_date)
    # converted_mins = convert_min_words(converted_date)
    print(convert_min_words(convert_date(handle_date(birth_date))))


# Check if the date passed by the user is valid per the regex expression.
def handle_date(birth_date):
    if not (date := re.search(r"(?P<year>^\d{4})-(?P<month>[1-9]|0?[1-9]|1[0-2])-(?P<day>0[1-9]|[1-2]\d|3[0-1])$", birth_date)):
        sys.exit("Invalid date")
    return f"{date.group('year')}-{date.group('month')}-{date.group('day')}"


# Converts the valid date passed from the handle_date function into minutes.
def convert_date(valid_date):
    year, month, day = valid_date.split("-")
    birth_date = date.fromisoformat(f"{year}-{month}-{day}")
    today_date = date.today()
    date_difference = today_date - birth_date
    date_difference_days = date_difference.days
    return date_difference_days * 24 * 60


# Utilizes the passed minutes from the convert_date function and converts them to words.
def convert_min_words(minute):
    p = inflect.engine()
    mins = p.number_to_words(minute, andword="")
    return f"{mins.capitalize()} minutes."


if __name__ == "__main__":
    main()