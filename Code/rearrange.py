import random
import sys

def rearrange(words):
    random.shuffle(words)
    return ' '.join(words)

if __name__ == '__main__':
    words = sys.argv[1:]
    rearranged_words = rearrange(words)
    print(rearranged_words)

# Or, without using the `shuffle` method:
# def rearrange(words):
#     rearranged_words = []
#     while len(words) > 0:
#         rand_index = random.randint(0, len(words) - 1)
#         rearranged_words.append(words.pop(rand_index))
#     return ' '.join(rearranged_words)
