import string
with open('moby.txt', 'r') as reader:
    with open('moby_clean.txt', 'w') as writer:
        text = reader.read()
        delete = str.maketrans({';': ' ', '.': ' ','-': ' ', ',': ' '})
        text= text.translate(delete).lower()
        for word in text.split(' '):
            if word != '':
                writer.write(str(word) + '\n')
