'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base case: no letter pairs left to iterate over
    if not word[:2]:
        return 0
    # getting closer to base case: iterate over letter pairs
    else:
        # if 'th' is in first two letters, return 1
        # and recurse on the rest of the word
        if word[:2] == 'th':
            return 1 + count_th(word[1:])
        else:
            return count_th(word[1:])
