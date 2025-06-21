#Random Name Picker
import random


def read_names_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            names = [name.strip() for name in data.split(';') if name.strip()]
            return names
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def get_random_names(names, count):
    if count > len(names):
        print("Requested number is greater than the available names. Showing all names instead.")
        return names
    return random.sample(names, count)


def main():
    filename = input("Enter the path to the text file containing names separated by ';': ")
    names = read_names_from_file(filename)

    if not names:
        print("No names found or file is empty.")
        return

    try:
        count = int(input(f"Enter number of random names to generate (max {len(names)}): "))
        if count < 1:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid number entered.")
        return

    selected_names = get_random_names(names, count)
    print("\nRandomly selected names:")
    for name in selected_names:
        print(f"- {name}")


if __name__ == "__main__":
    main()