import random
import sys

def rearrange(words):
    random.shuffle(words)
    return ' '.join(words)

if __name__ == '__main__':
    words = sys.argv[1:]
    rearranged_words = rearrange(words)
    print(rearranged_words)