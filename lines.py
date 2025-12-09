# To count number of lines of code, comments & blank lines from a python file

import sys

def main():
    file_names = sys.argv[1:]

    if validate_file_arguments(file_names):
        for file_name in file_names:
            code_lines, comments, blank_lines = count_lines(file_name)

            print(f"{file_name} contains:")
            print(f"{code_lines} lines of Code, {comments} lines of comments, {blank_lines} Blank lines")
            print()




def validate_file_arguments(file_names):
    if len(file_names) < 1:
        print("Too few command-line arguments!")
        sys.exit(1)

    for file_name in file_names:
        if not file_name.endswith(".py"):
            print("Invalid file name!")
            print("Usage: filename.py")
            sys.exit(2)

    return True


def open_and_read(file_name):
    try:
        with open(file_name) as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("File not found!")
        print("Please type valid file name")
        sys.exit(3)


def count_lines(file_name):
    code_lines = 0
    comments = 0
    blank_lines = 0

    lines = open_and_read(file_name)


    for line in lines:

        stripped_line = line.strip()

        if stripped_line.startswith("#"):
            comments += 1
        elif stripped_line == "":
            blank_lines += 1
        else:
            code_lines += 1

    return code_lines, comments, blank_lines




if __name__ == "__main__":
    main()
