import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments.")
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments.")
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file.")
    except Exception as e:
        print(e)
        sys.exit("Invalid Command Line Arguments.")
    else:
        print(line_counter(sys.argv[1]))

def line_counter(passed_file):
    try:
        with open(f"{passed_file}") as file:
            lines = 0
            for line in file:
                if line.isspace():
                    pass
                elif line.strip().startswith("#"):
                    pass
                else:
                    lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist.")
    else:
        return lines


if __name__ == "__main__":
    main()