# Nicolas Aguilar
# 06/02/2020

# Poem Mixer


poem = input('What is the poem?')
words_list = poem.split()
index = 0

for a in range(len(words_list)):
    if len(words_list[index]) <= 3:
        words_list[index] = words_list[index].lower()
    elif len(words_list[index]) >= 7:
        words_list[index] = words_list[index].upper()
    else:
        pass
    index += 1
    
print(words_list)

def word_mixer():
    words_list.sort()
    new_words = []
    while len(words_list) > 5:
        new_words.append(words_list.pop(4))
        new_words.append(words_list.pop(0))
        new_words.append(words_list.pop())
    return new_words
print(word_mixer())
