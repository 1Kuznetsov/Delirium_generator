from random import choice


def analysis():
    lst = []
    with open('input.txt') as f_in:
        numb = int(f_in.readline())
        for ptr in f_in:
            word = ''
            for i in range(len(ptr)):
                if i == len(ptr) and ptr[i] == '-' and word != 0:
                    continue
                if ptr[i].isalpha():
                    word += i
                else:
                    lst.append(word)
                    word = ''
    dictionary = {}
    for i in range(len(lst)):
        n = lst.pop(0)
        if n not in dictionary:
            dictionary[n] = lst
        else:
            continue
    return numb, dictionary

def delirium_generator(words_dict, cnt):
    txt = ''
    limit = 25
    sym_end = ['.', '?', '!']
    word = ''

    while cnt > 0:
        length = 0

        while length < limit:

            if length == 0:
                word = choice(words_dict.keys())

                while not word[0].isupper():
                    word = choice(words_dict.keys())

                txt += word

            else:
                last_word = word
                word = choice(words_dict[last_word])
                txt += word

            if word[-1] in sym_end:
                cnt -= 1
                break

        else:
            if txt[-1] not in sym_end:
                txt += '.'
                cnt -= 1

    return txt


if __name__ == '__main__':
    num, data = analysis()
    print(delirium_generator(data, num))
