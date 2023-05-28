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

def write_histogram_to_file(hist, filename):
    """
    This function takes a histogram and a filename, and writes the histogram to the file. Each line contains
    a word and its count, separated by a space.
    """
    with open(filename, 'w') as f:
        for word, count in hist.items():
            f.write(f'{word} {count}\n')


def read_histogram_from_file(filename):
    """
    This function takes a filename and returns a histogram (dictionary of word counts) based on the file.
    """
    hist = {}
    with open(filename, 'r') as f:
        for line in f:
            word, count = line.split()
            hist[word] = int(count)
    return hist

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
    with open('data/corpus.txt', 'r') as f:
        source_text = f.read()

    # Calculate the histogram
    hist = histogram(source_text)

    # Write the histogram to a file
    write_histogram_to_file(hist, 'data/histogram.txt')

    # Read the histogram from the file
    hist_from_file = read_histogram_from_file('data/histogram.txt')

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
