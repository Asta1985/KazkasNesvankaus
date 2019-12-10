import random

WORDLIST = 'zodziukai.txt'


def get_random_word(min_word_length):
    words = []
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            words.append(word)
    return random.choice(words)

