'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # base case
    if len(word) < 2:
        return 0
    # if first 2 letter contain 'th'
    if word[:2] == 'th':
        # return it and move to the next window
        return 1 + count_th(word[2:])
    else:
        # return starting at the index value of 1
        return 0 + count_th(word[1:])

