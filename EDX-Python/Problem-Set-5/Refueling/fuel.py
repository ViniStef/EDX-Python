# In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

# convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
# gauge expects an int and returns a str that is:
# "E" if that int is less than or equal to 1,
# "F" if that int is greater than or equal to 99,
# and "Z%" otherwise, wherein Z is that same int.
# def main():
#     ...


# def convert(fraction):
#     ...


# def gauge(percentage):
#     ...


# if __name__ == "__main__":
#     main()
# Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

def main():
    while True:
        fraction = input("Fraction: ").strip()
        convert(fraction)
        if type(convert(fraction)) == int:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        else:
            pass
 

def convert(fraction):
    try:
        X,Y = fraction.split("/")
        result = round(int(X) / int(Y), 2)
        if result < 0 or result > 1.00:
            return "Please enter a valid fuel fraction." 
        if result == 1.0:
            return 100
        else:
            value_percentage = str(result).split(".")[1]
            if len(value_percentage) == 1:
                return int(value_percentage) * 10 # f"{value_percentage}0%"
            elif int(value_percentage[0]) == 0:
                return int(value_percentage[1]) # f"{value_percentage[1]}%" 
            else:
                return int(value_percentage) # f"{value_percentage}%"     
    except (ValueError, ZeroDivisionError):
        pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()