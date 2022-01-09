"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
"""

def solution(s):
    list_pairs = []
    pair = ''
    for value in s:
        pair += value
        if len(pair) == 2:
            list_pairs.append(pair)
            pair = ''
    if pair:
        list_pairs.append(pair + '_')
    return list_pairs
