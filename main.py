from random import choice


def analysis():
    lst = []
    with open('input.txt') as f_in:
        numb = int(f_in.readline())
        # text = list(set(f_in.readline().split()))
        for ptr in f_in:
            word = ''
            for i in range(len(ptr)):
                if i == len(ptr) and ptr[i] == '-' and word != 0:
                    continue
                if not ptr[i] == '':
                    word += i
                else:
                    lst.append(word)
                    word = ''
    chain = {}
    for i in range(len(lst)):
        first = lst.pop(0)
        if first not in chain:
            chain[first] = lst
        else:
            continue
    return numb, chain

    # numb_text = len(text)
    # dictionary = {}
    # for i in text:
    #     if i not in dictionary:
    #         for j in range(numb_text):
    #             dictionary[j] = i
    # print(dictionary)


# text = list(set(input().split()))
numb = len(text)
dictionary = {}
for i in text:
    if i not in dictionary:
        for j in range(numb):
            dictionary[j] = i
print(dictionary)


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
    generated_text = delirium_generator(data, num)

    with open('output.txt', 'w') as f_out:
        f_out.write(generated_text)

