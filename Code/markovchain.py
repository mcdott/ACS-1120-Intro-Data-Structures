import random
import os

def learn_markov_chain(corpus):
    words = corpus.split(' ')
    m_dict = {}

    for i in range(len(words) - 1):
        if words[i] in m_dict:
            m_dict[words[i]].append(words[i + 1])
        else:
            m_dict[words[i]] = [words[i + 1]]

    return m_dict

def generate_sentence(markov_dict, num_words):
    current_word = random.choice(list(markov_dict.keys()))
    sentence = current_word

    for i in range(num_words - 1):
        if current_word in markov_dict:
            next_word = random.choice(markov_dict[current_word])
            sentence += ' ' + next_word
            current_word = next_word
        else:
            break

    return sentence

# Path to your text file
file_path = os.path.join('data', 'corpus.txt')

# Read the file
with open(file_path, 'r') as file:
    corpus = file.read()

# Learn the Markov Chain
markov_dict = learn_markov_chain(corpus)

# Generate a sentence
print(generate_sentence(markov_dict, 20))
