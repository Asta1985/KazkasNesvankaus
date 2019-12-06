import random
WORDLIST = 'wordlist.txt'

def get_random_word(min_word_length):
    words = []
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' or ')' in word:
                continue  # Skip the word because it contains parentheses.
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue  # Skip the word because it is too short.
            words.append(word)
    return random.choice(words)