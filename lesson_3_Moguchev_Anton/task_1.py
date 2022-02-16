def num_translate(eng):
    words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return words.get(eng)


print(num_translate(input('Enter number in English: ')))
