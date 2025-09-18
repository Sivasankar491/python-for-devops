import re


text = "The quick brown fox"
pattern = r"The" #match give TRUE only if it finds the pattren at the beginning of the line

match = re.match(pattern, text)

if match:
    print('match found', match.group())
else:
    print('no match found')