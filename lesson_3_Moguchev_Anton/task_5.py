import random


def jokes(*args):
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'позавчера', 'ночью', 'завтра']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
    joke = (random.choice(nouns), random.choice(adverbs), random.choice(adjectives))
    return joke


print(jokes())
