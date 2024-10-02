# Takes input string of two words separated by a comma, splits the string into two words,
# and prints the two words.

while True:
    text = input("Enter input string:\n")
    if text == 'q':
        break
    elif ',' in text:
        split_text = text.split(',')
        split_text[0] = split_text[0].strip()
        split_text[1] = split_text[1].strip()
        print("First word: " + split_text[0])
        print("Second word: " + split_text[1])
        print()
        continue
    
    else:
        print("Error: No comma in string.\n")
        continue
