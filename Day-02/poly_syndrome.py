text = input('enter a string: ')

ps = text[: : -1]

if ps == text:
    print('text is polysyndrome')
else:
    print('not polysyndrome')