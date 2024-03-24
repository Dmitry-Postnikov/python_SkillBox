designations = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
list_english_words = ['aden', 'diem', 'post', 'lodz']


def my_t9(old_str: str):
    count = 0
    new_str = ''
    for i in range(len(old_str) - 1):
        symbol = int(old_str[i])
        if symbol == 7 or symbol == 9:
            delit = 4
        else:
            delit = 3
        if old_str[i] == old_str[i + 1]:
            count += 1
        else:
            new_str += designations[symbol][count % delit]
            count = 0
    new_str += designations[int(old_str[-1])][count % delit]
    lst = []
    for word in list_english_words:
        if word[0] == new_str[0] and word[-1] == new_str[-1] \
                and len(word) - 3 < len(word) < len(new_str) + 3:
            lst.append(word)
    print('Принимаемая на вход строка:', old_str)
    print('Строка, полученная при полном использовании цифр из принимающей строки:', new_str)
    print('Слова, которые могут получиться:', ''.join(lst))


my_t9("766677778")