def count_char(string):
    char_count = {}
    symbol = []
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
        if char_count[char] > 1:
            symbol.append(')')
        else: symbol.append('(')
    return ('').join(symbol)

print(count_char('subinkhatiwadaisagoodman'))