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
    
    def clean_text(self):
        corpus = self.read_file()
        corpus = self.remove_unwanted_punctuation(corpus)
        corpus = self.standardize_quotes(corpus)
        return corpus
    
# Usage
parser = TextParser('data/corpus.txt')
clean_corpus = parser.clean_text()
print(clean_corpus)