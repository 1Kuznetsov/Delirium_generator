# Kuznetsov Igor - 100, Yadreeva Maria - 63.

from random import choice


def analysis():
    lst = []

    with open('input.txt', 'r', encoding='utf8') as f_in:
        numb = int(f_in.readline())

        for ptr in f_in:
            word = ''
            for i in range(len(ptr)):
                if i == len(ptr)-1 and ptr[i] == '-' and word != '':
                    continue

                if ptr[i] != ' ':
                    word += ptr[i]

                elif word != '':
                    word = word.replace('\n', '')

                    if word != '':
                        lst.append(word)
                        word = ''

                if i == len(ptr)-1:
                    word = word.replace('\n', '')

                    if word != '':
                        lst.append(word)
                        word = ''

    if word != '':
        lst.append(word)

    chain = {}

    for i in range(len(lst) - 1):
        first = lst.pop(0)

        if first not in chain.keys():
            chain[first] = [lst[0]]

        else:
            chain[first].append(lst[0])

    return numb, chain


def delirium_generator(words_dict, cnt):
    txt = ''
    limit = 25
    sym_end = ['.', '?', '!']
    word = ''

    while cnt > 0:
        length = 0

        while length < limit:

            if length == 0:
                word = choice(list(words_dict.keys()))

                while not word[0].isupper():
                    word = choice(list(words_dict.keys()))

                txt += word
                txt += ' '
                length += 1

            else:
                last_word = word
                word = choice(words_dict[last_word])

                txt += word
                txt += ' '
                length += 1

            if word[-1] in sym_end:
                cnt -= 1
                break

        else:
            if txt[-1] not in sym_end:
                txt = txt + '.'
                cnt -= 1

    return txt


if __name__ == '__main__':
    num, data = analysis()

    generated_text = delirium_generator(data, num)

    with open('output.txt', 'w', encoding='utf8') as f_out:
        f_out.write(generated_text)
