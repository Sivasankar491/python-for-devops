import re

string = "The quick brown fox jumps over the lazy brown dog"

pattren = 'brown'
replacement = 'red'
sub_string = re.sub(pattren, replacement, string)

print(sub_string)