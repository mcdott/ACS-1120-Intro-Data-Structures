import random
import os
import string

class MarkovSentenceGenerator:
    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.markov_dict = self.learn_markov_chain()


    def learn_markov_chain(self):
        with open(self.corpus_path, 'r') as file:
            corpus = file.read()
        words = corpus.split(' ')
        markov_dict = {}

        for i in range(len(words) - 1):
            if words[i] in markov_dict:
                markov_dict[words[i]].append(words[i + 1])
            else:
                markov_dict[words[i]] = [words[i + 1]]

        return markov_dict
    
    def clean_sentence(self, sentence):
        # Remove all punctuation except commas
        sentence = ''.join(ch if ch not in string.punctuation or ch == ',' else ' ' for ch in sentence)

        # Capitalize the first letter and add exclamation mark at the end
        sentence = sentence.capitalize().strip() + '!'
        
        return sentence

    def generate_sentence(self, num_words):
        current_word = random.choice(list(self.markov_dict.keys()))
        sentence = current_word

        for i in range(num_words - 1):
            if current_word in self.markov_dict:
                next_word = random.choice(self.markov_dict[current_word])
                sentence += ' ' + next_word
                current_word = next_word
            else:
                break

        return self.clean_sentence(sentence)

# Usage
file_path = os.path.join('data', 'corpus.txt')
generator = MarkovSentenceGenerator(file_path)
print(generator.generate_sentence(20))
