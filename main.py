
def example_a():
    print('\nExample A')
    print('~~~~~~~~~')

    choice = input("Would you rather be a Parking Enforcement Officer or a Clown?: ")

    # String Concatenation
    # Add the variable "choice" onto the end of the string
    print('You chose: ' + choice)
    print('But it was a trick question, they are BOTH clowns')

# Puzzle A - Your favourite color
#
# Write a program that asks for your favourite color.
# It should output "Your favorite color is " and then their fav color
# Use String Interpolation to print the answer, not string concatenation as shown above.
# There are three types, f'blah blah blah {var}' and .format() and %s
def puzzle_a():
    print('\nPuzzle A')
    print('~~~~~~~~~~~')


def example_b():
    print('\nExample B')
    print('~~~~~~~~~~~')

    message = 'I wish I had chainsaws for hands, or at least nuclear arms.'

    print(message)
    print("Converted to all lowercase: " + message.lower())


# Puzzle B - I was too sick to do my homework
#
# Write a program that displays the message
# "I was too sick to do my homework."
# Then display this same message in all capitals (uppercase).
# Use string interpolation again, not concatenation as shown in Example B.
def puzzle_b():
    print('\nPuzzle B')
    print('~~~~~~~~~~~')


def example_c():
    print('\nExample C')
    print('~~~~~~~~~~~')

    fav_food = input("What's your favourite food?: ")

    fav_drink = input("What's your favourite drink?: ")

    print(f"If I was to take you on a date, we would have {fav_food} and {fav_drink}.")
    print('But you are far too ugly for me to ask you on a date.')


# Puzzle C – Folder Names
#
# Ask the user to input a folder name
# Then ask the user to input a file name
# Display the file path "C:\{folder_name}\{file_name}.txt" using the user's inputs
# You will need to learn how to escape the backslash characters or use raw strings.
def puzzle_c():
    print('\nPuzzle C')
    print('~~~~~~~~~~~')


if __name__ == '__main__':

    # Run the puzzles

    example_a()
    # puzzle_a()

    example_b()
    # puzzle_b()

    example_c()
    # puzzle_c()
