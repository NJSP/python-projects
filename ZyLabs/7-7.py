# takes a character and a string as input and counts the number of times the 
# character appears in the string

text = input()
split_text = text.split(' ', 1)
count = 0
for i in split_text[1]:
    if i == split_text[0]:
        count += 1

if count == 0:
    print(0, split_text[0] + "'s")
elif count == 1:
    print(1, split_text[0])
elif count > 1:
    print(count, split_text[0] + "'s")