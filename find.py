# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    # TODO: add an optional flag -i / --ignore-case  (use action="store_true")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="ignore case when matching")
    args = parser.parse_args()

    # TODO: 
    lines = open(args.filename)
    for line_number, line in enumerate(lines, start=1):

        line=line.rstrip("\n")
        if args.ignore_case:
            if args.pattern.lower() in line.lower():
                print(str(line_number) + ": " + line)
        else:
            if args.pattern in line:
                print(str(line_number) + ": " + line)

if __name__ == "__main__":
    main()
