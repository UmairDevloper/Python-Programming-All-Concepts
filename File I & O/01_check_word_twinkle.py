f = open("poem.txt", 'r')

content = 'twinkle'

for word in f:
    if content in word:
        print(word)

f.close()