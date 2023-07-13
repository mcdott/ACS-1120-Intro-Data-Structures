import random
import string

class MarkovSentenceGenerator:
    def __init__(self, tokenized_corpus):
        self.tokenized_corpus = tokenized_corpus
        self.markov_dict = self.learn_markov_chain()


    def learn_markov_chain(self):
        words = self.tokenized_corpus
        markov_dict = {}

        for i in range(len(words) - 3):
            triple = (words[i], words[i + 1], words[i + 2])
            if triple in markov_dict:
                markov_dict[triple].append(words[i + 3])
            else:
                markov_dict[triple] = [words[i + 3]]

        return markov_dict
    
    def punctuate_sentence(self, sentence):
        # Capitalize the first letter and add exclamation mark at the end
        sentence = sentence[0].upper() + sentence[1:].strip() + '!'
        
        return sentence


    def generate_sentence(self, num_words):
        current_triple = random.choice(list(self.markov_dict.keys()))
        sentence = current_triple[0] + ' ' + current_triple[1] + ' ' + current_triple[2]

        for i in range(num_words - 3):
            if current_triple in self.markov_dict:
                next_word = random.choice(self.markov_dict[current_triple])
                sentence += ' ' + next_word
                current_triple = (current_triple[1], current_triple[2], next_word)
            else:
                break

        return self.punctuate_sentence(sentence)