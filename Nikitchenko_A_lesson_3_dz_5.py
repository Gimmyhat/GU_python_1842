from random import choice, shuffle


def get_jokes(n=2, no_repeat=True):
    """
    Функция возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if n > 5:  n = 5
    if no_repeat:  # запрещены повторы слов в шутках
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        joke = [(nouns[i] + ' ' + adverbs[i] + ' ' + adjectives[i]) for i in range(n)]
    else:  # разрешены повторы слов в шутках
        joke = [(choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)) for i in range(n)]
    return joke

print(get_jokes(5, True))
