import itertools

first_letter = lambda str: str[0]

words = ['Pat', 'Cake', 'Pill', 'Tap', 'Ramp', 'Coal']

for starts_with, words in itertools.groupby(words, first_letter):
    print(starts_with, list(words)) 
