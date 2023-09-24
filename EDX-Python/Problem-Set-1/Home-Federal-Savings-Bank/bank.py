# In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
import re


def main():
    print(check_greeting(input("Greeting: ").strip().lower()))


def check_greeting(greeting) -> str:
    # Check if theres a number, if there is just return a message indicating it.
    if check_valid := re.search(r"[^\d]+", greeting, re.IGNORECASE):
        if greeting.startswith("hello"):
            return "$0"
        elif greeting.startswith("h"):
            return "$20"
        else:
            return "$100"
    else:
        return "Numbers not allowed."


if __name__ == "__main__":
    main()