#When you prefix a string with r (or R), the backslashes within that string are interpreted literally. 
# They do not trigger escape sequence processing.
import re
str = "the brown quick fox"

pattern = r'brown'

search = re.search(pattern, str)
if search:
    print('match found', search.group())
else:
    print('no match')