"""Main script, uses other modules to generate sentences."""
from flask import Flask
from cleanup import TextParser
from tokens import TextTokenizer
from sentence import MarkovSentenceGenerator

app = Flask(__name__)

# Prepare the corpus and initialize markov chain.
# This code will run only once, when the server starts.
corpus_path = 'corpus.txt'
preparred_corpus_path = 'preparred_corpus.txt'

# Clean the corpus
parser = TextParser(corpus_path)
parser.save_preparred_text(preparred_corpus_path)

# Tokenize the cleaned corpus
with open(preparred_corpus_path, 'r') as file:
    preparred_corpus = file.read()
tokenizer = TextTokenizer(preparred_corpus)
tokenized_corpus = tokenizer.tokenize()

# Generate sentences
tweet_generator = MarkovSentenceGenerator(tokenized_corpus)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = tweet_generator.generate_sentence(20)
    return f"<p>{sentence}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
