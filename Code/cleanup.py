import re

class TextParser:

    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.common_wonderland_words = {
            'White Rabbit': 'Hareflustious',
            'Queen of Hearts': 'Queebeheaderous',
            'King of Hearts': 'King Mildemane',
            'Cheshire Cat': 'Grinsvanishire',
            'Mad Hatter': 'Teatimzy Lunatico',
            'Hatter': 'Teatimzy',
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
            'Wonderland': 'Jabberland',
            'Rabbit Hole': 'Raburrow',
            'The Pool of Tears': 'Weepuddle',
            'The Caucus Race': 'Rundebate',
            'The Duchess\'s Kitchen': 'Cookduchery',
            'Mad Tea-Party': 'Lunachai',
            'Queen\'s Croquet Ground': 'Quequet Field',
            'The Mock Turtle\'s Story': 'Tale-Turtlery',
            'The Lobster Quadrille': 'Lobstrance',
            'The Knave of Hearts\' Trial': 'Justiknavery',
            'The White Rabbit\'s House': 'Bunnicottage',
            'Eat Me Cake': 'Ingestibake',
            'Drink Me Potion': 'Sipsolution',
            'Cheshire Cat\'s Grin': 'Smileshire',
            'Tarts of the Queen': 'Queentreats',
            'Flamingo': 'Flamingleap',
            'Hedgehog': 'Spinecurl',
            'Puppy': 'Puppounce',
            'Fish': 'Fisplash',
            'Frog': 'Leapcroak',
            'Pig': 'Snoutgrunt',
            'Baby': 'Babblooth',
            'Pigeon': 'Cooclaw',
            'Lory': 'Lorflutter',
            'Duck': 'Quackfloat',
            'Crab': 'Crabscuttle',
            'Owl': 'Hootstare',
            'Panther': 'Prowlur',
            'Eaglet': 'Eaglide',
            'Rose': 'Rosprickle',
            'Violet': 'Violethide',
            'Lily': 'Lilglisten',
            'Daisy': 'Daisglow',
            'slimy': 'slithy',
            'lithe': 'slithy',
            'gyrate': 'gyre',
            'dire': 'gyre',
            'gimlet': 'gimble',
            'nimble': 'gimble',
            'miserable': 'mimsy',
            'flimsy': 'mimsy',
            'bore': 'borogove',
            'grove': 'borogove',
            'from home': 'mome',
            'rath': 'rath',
            'wraith': 'rath',
            'outgribe': 'outgrabe',
            'grave': 'outgrabe',
            'jubilant': 'jubjub',
            'stubborn': 'jubjub',
            'furious': 'frumious',
            'fuming': 'frumious',
            'gruffish': 'uffish',
            'huffish': 'uffish',
            'hurrah': 'callooh',
            'hallelujah': 'callooh',
            ' oh ': ' callay ',
            'yay': 'callay',
            'time': 'timension',
            'eyes': 'eyescapes',
            'door': 'doorniverse',
            ' day ': ' daydreamsicle ',
            'white': 'whilight',
            'large': 'largeful',
            'small': 'smallsome',
            'round': 'roundorama',
            'book': 'booksplore',
            ' arm': ' armstrong',
            'feet': 'feetstumps',
            'garden': 'gardenchant',
            'heart': 'heartmosphere',
            'game': 'gamestacy',
            'see ': 'seeclipse ',
            'never': 'neverdawn',
            'thought': 'thoughtrain',
            'looked': 'looklusioned',
            'must ': 'mustmuse ',
            ' head': ' headventure',
            'voice': 'voiceloom',
            'began': 'begantic',
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
    
    def remove_chapter_headings(self, corpus):
        # Regex to match "CHAPTER " followed by one or more Roman numerals
        return re.sub(r'CHAPTER [IVXLC]+', '', corpus)
    
    def jabberize_common_wonderland_words(self, corpus):
        for wonderland_word, jabberized_word in self.common_wonderland_words.items():
            corpus = corpus.replace(wonderland_word, jabberized_word)
        return corpus
    
    def cleaned_jabberized_text(self):
        corpus = self.read_file()
        corpus = self.remove_unwanted_punctuation(corpus)
        corpus = self.standardize_quotes(corpus)
        corpus = self.jabberize_common_wonderland_words(corpus)
        return corpus
    
    def save_cleaned_jabberized_text(self, output_filename):
        jabberized_corpus = self.cleaned_jabberized_text()
        with open(output_filename, 'w') as file:
            file.write(jabberized_corpus)