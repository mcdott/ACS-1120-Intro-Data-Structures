import random
import sys

def random_word(filename):
    # Open the file
    with open(filename, 'r') as f:
        # Read the file and split lines
        lines = f.readlines()

    # Get the words only (ignoring the counts)
    words = [line.split()[0] for line in lines]

    # Generate a random index based on the length of words
    random_index = random.randint(0, len(words) - 1)

    # Return a random word
    return words[random_index]

if __name__ == "__main__":
    # pass in the path to the text file as an argument
    print(random_word(sys.argv[1]))
