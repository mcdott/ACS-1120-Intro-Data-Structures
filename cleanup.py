class TextParser:

    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.character_names = {
            'Alice': 'Riddlishy',
            'White Rabbit': 'Hareflustious',
            'Queen of Hearts': 'Queebeheaderous',
            'King of Hearts': 'King Mildemane',
            'Cheshire Cat': 'Grinsvanishire',
            'Mad Hatter': 'Teatimzy Lunatico',
            'March Hare': 'Springbound Nuttersly',
            'Dormouse': 'Dozesqueakle',
            'Caterpillar': 'Puffosophor',
            'Duchess': 'Duchiwrath',
            'Knave of Hearts': 'Knave Tartsnatcher',
            'Tweedledee': 'Dumbleriddle',
            'Tweedledum': 'Dumblerumble',
            'Mock Turtle': 'Turtly Facado',
            'Gryphon': 'Eaglionix',
            'Bill the Lizard': 'Lizascaler Billius',
            'Dodo': 'Dodgsonic',
            'Mouse': 'Rodentiquake',
        }

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
    
    def replace_character_names(self, corpus):
        for original_name, jabbercised_name in self.character_names.items():
            corpus = corpus.replace(original_name, jabbercised_name)
        return corpus
    
    def preparred_text(self):
        corpus = self.read_file()
        corpus = self.remove_unwanted_punctuation(corpus)
        corpus = self.standardize_quotes(corpus)
        corpus = self.replace_character_names(corpus)
        return corpus
    
    def save_preparred_text(self, output_filename):
        preparred_corpus = self.preparred_text()
        with open(output_filename, 'w') as file:
            file.write(preparred_corpus)