def num_translate(num):
    dictionary = dict (one='один', two='два', three='три', four='четыре', five='пять', six='шесть',
                       seven='семь', eight='восемь', nine='девять', ten='десять')
    if num.istitle():
        return dictionary.get (num.lower ()).title()
    return dictionary.get (num.lower ())


print (num_translate (input ('Напишите число по английски: ')))
