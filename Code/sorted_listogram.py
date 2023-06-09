from listogram import Listogram


class SortedListogram(Listogram):
    """Listogram implemented as a list of (word, count) tuples that are kept in alphabetical order of word"""
    def __init__(self, word_list=None):
        super(SortedListogram, self).__init__(word_list)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount.  If word is not in the list,
        calls `insert_word` to insert it at the correct position in the alphabetically sorted list."""
        index = self.index_of(word)
        if index is None:
            self.insert_word(word, count)
            self.types += 1
        else:
            word, freq = self[index]
            self[index] = (word, freq + count)
        self.tokens += count

    def insert_word(self, word, count=1):
        """Insert word in sorted alphabetical order"""
        if len(self) == 0:
            self.append((word, count))
        else:
            for i in range(len(self)):
                if word < self[i][0]:
                    self.insert(i, (word, count))
                    return
            self.append((word, count))

    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found. 
        (Uses binary search.  Keeps list sorted in alphabetical order.)"""
        lower_bound = 0
        upper_bound = len(self) - 1
        while lower_bound <= upper_bound:
            middle_index = (upper_bound + lower_bound) // 2
            middle_value = self[middle_index][0]
            if middle_value == target:
                return middle_index
            elif middle_value < target:
                lower_bound = middle_index + 1
            else:
                upper_bound = middle_index - 1
        return None

def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = SortedListogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = SortedListogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram:
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()