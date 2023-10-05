# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

# def main():
#     ...


# def is_valid(s):
#     ...


# if __name__ == "__main__":
#     main()
# Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_plates.py
import string

def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_valid_length(s):
        if two_letters_start(s):
            if middle_number_check(s):
                if number_or_letter(s):
                    return True
                else:
                    return False

    return False

def is_valid_length(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True
    

def two_letters_start(s):
        try:
            _ = int(s[0])
        except ValueError:
            try:
                _ = int(s[1])
                return False
            except ValueError:
                return True
        return False


def middle_number_check(s):
    numbers = [i for i in range(10)]
    num_appear = False
    for current_index, value in enumerate(s):
        if int(current_index) > 1:
            try:
                if not num_appear:
                    if int(value) == 0:
                        return False
                    else:
                        num_appear = True
                if int(value) in numbers:
                    if current_index != len(s)-1:
                        try:
                            if int(s[int(current_index)+1]) in numbers:
                                continue
                        except ValueError:
                            return False
                    else:
                        return True
            except ValueError:
                pass
        else:
            pass

def number_or_letter(s):
    letters = list(string.ascii_uppercase)
    numbers = [i for i in range(10)]
    for i in s:
        try:
            if i in letters or int(i) in numbers:
                continue
            else:
                return False
        except ValueError:
            return False
    return True


if __name__ == "__main__":
    main()