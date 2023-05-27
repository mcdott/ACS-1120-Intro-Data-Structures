import string

def histogram(source_text):
    """
    This function takes a string as input, and processes the string to return a histogram as a dictionary.
    """
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    source_text = source_text.translate(translator).lower()

    # Create a histogram
    word_counts = {}
    for word in source_text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def unique_words(hist):
    """
    This function takes a histogram (dictionary of word counts) and returns the number of unique words.
    """
    return len(hist)


def frequency(word, hist):
    """
    This function takes a word and a histogram (dictionary of word counts), and returns the frequency of that word.
    """
    return hist.get(word, 0)


def main():
    # Read the text file
    with open('data/sample.txt', 'r') as f:
        source_text = f.read()

    # Calculate the histogram
    hist = histogram(source_text)

    print("Number of unique words:", unique_words(hist))
    print("Frequency of 'bottle':", frequency('bottle', hist))

    # Compute some statistics
    values = list(hist.values())
    mean = sum(values) / len(values)
    median = sorted(values)[len(values) // 2]
    mode = max(set(values), key=values.count)
    
    print("Mean word frequency:", mean)
    print("Median word frequency:", median)
    print("Mode word frequency:", mode)


if __name__ == "__main__":
    main()
