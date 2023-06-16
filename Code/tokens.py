import re

def tokenize(text):
    tokens = split_on_whitespace(text)
    return tokens

def split_on_whitespace(text):
    return re.split('\s+', text)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename given as argument')