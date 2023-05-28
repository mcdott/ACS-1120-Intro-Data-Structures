import random
import sys

def weighted_random_word(filename):
    # Open the file
    with open(filename, 'r') as f:
        # Read the file and split lines
        lines = f.readlines()

    # Convert lines to a dictionary
    histogram = {line.split()[0]: int(line.split()[1]) for line in lines}

    # Calculate the sum of all frequencies
    total = sum(histogram.values())

    # Generate a random number between 0 and the total
    rand = random.randint(0, total - 1)

    # Subtract each word's frequency from the random number until we reach 0
    # (words with higher frequencies will fill a larger range in this interval 
    # and are more likely to be chosen)
    for word, freq in histogram.items():
        rand -= freq
        if rand < 0:
            return word

if __name__ == "__main__":
    print(weighted_random_word(sys.argv[1]))




# Generate a single random word from a text file
# import random
# import sys

# def random_word(filename):
#     # Open the file
#     with open(filename, 'r') as f:
#         # Read the file and split lines
#         lines = f.readlines()

#     # Get the words only (ignoring the counts)
#     words = [line.split()[0] for line in lines]

#     # Generate a random index based on the length of words
#     random_index = random.randint(0, len(words) - 1)

#     # Return a random word
#     return words[random_index]

# if __name__ == "__main__":
#     # pass in the path to the text file as an argument
#     print(random_word(sys.argv[1]))
