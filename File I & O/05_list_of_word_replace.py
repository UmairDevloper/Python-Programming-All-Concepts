
words = ['Donkey', 'fool', 'ganda']

for word in words:
    with open('donkeyfile.txt', 'r') as f:
        content = f.read()
        contentNew = content.replace(word, '#' * len(word))
        with open('donkeyfile.txt', 'w') as f:
            f.write(contentNew)