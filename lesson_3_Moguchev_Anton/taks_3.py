import pprint


def thesaurus(*args):
    colleagues = dict()
    for name in args:
        letters = name[0]
        if letters not in colleagues:
            colleagues[letters] = []
        colleagues[letters].append(name)
    return colleagues


pprint.pprint(thesaurus('Иван', 'Илья', 'Катя', 'Маша', 'Максим'), width=1)
