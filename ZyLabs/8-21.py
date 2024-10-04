# Write a program that reads a list of words. Then, the program outputs those words and their frequencies (case insensitive).

def main():
    words = input().split()
    word_freq = {}
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    for word in words:
        print(word, word_freq[word.lower()])

if __name__ == '__main__':
    main()