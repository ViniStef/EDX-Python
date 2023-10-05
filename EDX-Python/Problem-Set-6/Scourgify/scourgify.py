# “Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with a bit of cleaning, too.” She pointed her wand at Hedwig’s cage. “Scourgify.” A few feathers and droppings vanished.

# — Harry Potter and the Order of the Phoenix

# Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:

# name,house
# "Abbott, Hannah",Hufflepuff
# "Bell, Katie",Gryffindor
# "Bones, Susan",Hufflepuff
# "Boot, Terry",Ravenclaw
# "Brown, Lavender",Gryffindor
# "Bulstrode, Millicent",Slytherin
# "Chang, Cho",Ravenclaw
# "Clearwater, Penelope",Ravenclaw
# "Crabbe, Vincent",Slytherin
# "Creevey, Colin",Gryffindor
# "Creevey, Dennis",Gryffindor
# "Diggory, Cedric",Hufflepuff
# "Edgecombe, Marietta",Ravenclaw
# "Finch-Fletchley, Justin",Hufflepuff
# "Finnigan, Seamus",Gryffindor
# "Goldstein, Anthony",Ravenclaw
# "Goyle, Gregory",Slytherin
# "Granger, Hermione",Gryffindor
# "Johnson, Angelina",Gryffindor
# "Jordan, Lee",Gryffindor
# "Longbottom, Neville",Gryffindor
# "Lovegood, Luna",Ravenclaw
# "Lupin, Remus",Gryffindor
# "Malfoy, Draco",Slytherin
# "Malfoy, Scorpius",Slytherin
# "Macmillan, Ernie",Hufflepuff
# "McGonagall, Minerva",Gryffindor
# "Midgen, Eloise",Gryffindor
# "McLaggen, Cormac",Gryffindor
# "Montague, Graham",Slytherin
# "Nott, Theodore",Slytherin
# "Parkinson, Pansy",Slytherin
# "Patil, Padma",Gryffindor
# "Patil, Parvati",Gryffindor
# "Potter, Harry",Gryffindor
# "Riddle, Tom",Slytherin
# "Robins, Demelza",Gryffindor
# "Scamander, Newt",Hufflepuff
# "Slughorn, Horace",Slytherin
# "Smith, Zacharias",Hufflepuff
# "Snape, Severus",Slytherin
# "Spinnet, Alicia",Gryffindor
# "Sprout, Pomona",Hufflepuff
# "Thomas, Dean",Gryffindor
# "Vane, Romilda",Gryffindor
# "Warren, Myrtle",Ravenclaw
# "Weasley, Fred",Gryffindor
# "Weasley, George",Gryffindor
# "Weasley, Ginny",Gryffindor
# "Weasley, Percy",Gryffindor
# "Weasley, Ron",Gryffindor
# "Wood, Oliver",Gryffindor
# "Zabini, Blaise",Slytherin
# Source: en.wikipedia.org/wiki/List_of_Harry_Potter_characters

# Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

# Dear Potter, Harry,

# Rather than with, for instance:

# Dear Harry,

# In a file called scourgify.py, implement a program that:

# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import csv
import sys

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments.")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments.")
        else:
            output_file(sys.argv[2], input_file(sys.argv[1]))
    except Exception as e:
        print(sys.argv[1], sys.argv[2])
        sys.exit(f"Something went wrong. Error: {e}")


def input_file(e_csv):
    try:
        students = []
        with open(e_csv) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        sys.exit("Could not read " + e_csv)
    else:
        return students


def output_file(new_csv_file,students_info):

    with open(new_csv_file, "a", newline="") as file:
        students= []
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first","last": "last","house": "house"})
        for student in students_info:
            last, first = student["name"].rstrip().split(", ")
            # print(first,last,student["house"])
            students.append({"first": first, "last": last, "house": student["house"]})

        for student in sorted(students, key=lambda student: student["first"]):
            writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})


if __name__ == "__main__":
    main()