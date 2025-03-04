def count_words(f):
    
    with open(f, 'r') as file:
        word_count = 0
        for line in file:
            words = line.strip().split()
            word_count += len(words)
        return word_count

f = input('Enter the file name: ')
word_count = count_words(f)
print(word_count)