"""
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.

Dada uma sequência de palavras, você precisa encontrar a palavra com maior pontuação.
Cada letra de uma palavra marca pontos de acordo com sua posição no alfabeto: a = 1, b = 2, c = 3 etc.
Você precisa retornar a palavra de pontuação mais alta como uma string.
Se duas palavras tiverem a mesma pontuação, retorne a palavra que aparece primeiro na string original.
Todas as letras serão minúsculas e todas as entradas serão válidas.
"""


def high(words):
    alpha = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    record = 0
    for w in words.split():
        score = 0
        for l in w:
            if l in alpha:
                score += alpha[l]
        if score > record:
            record = score
            word_list = []
            word_list.append(w)
        elif score == record:
            record = score
            word_list.append(w)
    return word_list[0]
