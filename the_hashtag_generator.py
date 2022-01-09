"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
"""

# My answer
def generate_hashtag(s):
    if len(s) == 0:
        return False
    s_split = s.split()
    s_final = '#'
    for value in s_split:
        s_final += value.capitalize()
    if len(s_final) > 140:
        return False
    else:
        return s_final

# Another answer
"""
def generate_hashtag(s):
    output = "#"
    for word in s.split():
        output += word.capitalize()
    return False if (len(s) == 0 or len(output) > 140) else output
"""