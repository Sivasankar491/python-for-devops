str1 = "hello"
str2 = "world"

full = str1,str2
print(full)
print(type(full))

complete = str1 + " " + str2
print(complete)

print(f'length of complete:', len(complete))

print(f'lenghth, {len(complete)}')

new_word = complete.replace("world", "beautiful")
print(new_word)

split_string= new_word.split('u')
print(split_string)