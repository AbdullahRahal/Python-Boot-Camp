def checking (guess, chosen_word, blanks):
    i = 0
    for letter in chosen_word:
        if letter == guess:
            blanks[i] = guess
        i += 1