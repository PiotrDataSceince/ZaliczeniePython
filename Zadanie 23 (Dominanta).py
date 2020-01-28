from collections import Counter

lista = [0.5, 0.4, 0.3, 1.3, 1.4]


def dominanta(x):
    c = Counter(x)
    return c.most_common(1)[0][0]


a = dominanta(lista)

print(a)

