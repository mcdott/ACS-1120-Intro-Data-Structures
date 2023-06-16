class TextParser:

    def __init__(self, corpus_path):
        self.corpus_path = corpus_path

    def read_file(self):
        with open(self.corpus_path, 'r') as file:
            corpus = file.read()
        return corpus
    
    def remove_unwanted_punctuation(self, corpus):  
        unwanted_punctuation = ['_', '*']
        for mark in unwanted_punctuation:
            corpus = corpus.replace(mark, '')
        return corpus
       
    def standardize_quotes(self, corpus):
        corpus = corpus.replace('“', '"')
        corpus = corpus.replace('”', '"')
        corpus = corpus.replace('‘', "'")
        corpus = corpus.replace('’', "'")
        return corpus
    
# Usage
parser = TextParser('data/corpus.txt')
corpus = parser.read_file()
corpus = parser.remove_unwanted_punctuation(corpus)
corpus = parser.standardize_quotes(corpus)
print(corpus)