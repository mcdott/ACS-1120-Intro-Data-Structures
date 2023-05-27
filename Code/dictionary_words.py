import random
import sys

def generate_word_salad(num_words):
    with open('/usr/share/dict/words', 'r') as dictionary:
        words = dictionary.read().splitlines()

    chosen_words = random.sample(words, num_words)
    return chosen_words

if __name__ == "__main__":
    num_words = int(sys.argv[1])
    word_salad = generate_word_salad(num_words)
    print(' '.join(word_salad) + '.')
