def capitalize(string):
    word_list = string.split(' ')       # re.split behaves as expected
    final = []
    for word in word_list:
        final.append(word.capitalize() )
    
    return " ".join(final)