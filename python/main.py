word = input("Enter a word you would like to count... Whitespace is ignored: ")
sum = 0

for i in word:
    if i == ' ':
        pass
    else:
        sum += 1
print(f"There are {sum} alphabet in the word: \"{word}\" excluding whitespaces")