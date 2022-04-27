yesWord = 'y'
wordsList = list()

while yesWord.upper() == 'Y':
    word = str(input('Enter a word: '))
    print(f'You entered {word}')
    wordsList.append(word)
    yesWord = str(input('Do you want to try again? [Y/N]'))

print(f'You entered {len(wordsList)} words: {wordsList}')