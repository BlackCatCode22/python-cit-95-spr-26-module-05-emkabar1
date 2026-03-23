import re

count = 0
regex = input('Enter a regular expression:')
hand = open('mbox.txt')
for line in hand:
    if re.search(regex, line):
        count += 1

print('mbox.txt had', count, 'lines that matched', regex)
