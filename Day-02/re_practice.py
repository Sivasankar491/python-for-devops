import re


text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)

if search:
    print('match found', search.group())
else:
    print('no match found')