import string

# Write a program that reads a list of words. Then, the program outputs those words and their frequencies (case insensitive).


def count_word_frequencies(input_string):
    words = input_string.split()
    word_freq = {}
    for word in words:
        word = word.lower().strip(string.punctuation)
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    for word in words:
        clean_word = word.lower().strip(string.punctuation)
        print(f"{word} ({clean_word}): {word_freq[clean_word]}")

if __name__ == '__main__':
    count_word_frequencies('This is a Big big string with a A lot of not very big words.')
    count_word_frequencies('Hello, world! Hello, universe! Hello... everyone.')