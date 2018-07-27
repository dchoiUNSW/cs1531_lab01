strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for x in strings:
    sentence = sentence + x + ' '

print(sentence[:-1])
print(' '.join(strings))
