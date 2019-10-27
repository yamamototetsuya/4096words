#!py -3

import json

words = []
for line in open('words.txt', encoding='utf-8'):
    a = line[:-1].split(" ")
    if a[-1]:
        words.append(a[-1])

print("var words = " + json.dumps(words))
