word = input('enter a word: ')
first = word[0]
length = len(word)
left = word[1:length]

if first != 'a' and first != 'e' and first != 'i' and first != 'o' and first != 'u':
    new_word = left + first + "ay"
else:
    new_word = word + "way"
print(new_word.lower())
