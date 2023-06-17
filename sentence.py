import random

class MarkovSentenceGenerator:
    def __init__(self, tokenized_corpus):
        self.tokenized_corpus = tokenized_corpus
        self.markov_dict = self.learn_markov_chain()


    def learn_markov_chain(self):
        words = self.tokenized_corpus
        markov_dict = {}

        for i in range(len(words) - 2):
            pair = (words[i], words[i + 1])
            if pair in markov_dict:
                markov_dict[pair].append(words[i + 2])
            else:
                markov_dict[pair] = [words[i + 2]]

        return markov_dict

    def generate_sentence(self, num_words):
        current_pair = random.choice(list(self.markov_dict.keys()))
        sentence = current_pair[0] + ' ' + current_pair[1]

        for i in range(num_words - 2):
            if current_pair in self.markov_dict:
                next_word = random.choice(self.markov_dict[current_pair])
                sentence += ' ' + next_word
                current_pair = (current_pair[1], next_word)
            else:
                break

        return sentence