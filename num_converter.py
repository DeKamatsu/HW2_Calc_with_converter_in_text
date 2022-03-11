# converter of num to text
# author: Denis Matveev
# ver.2022.03.09

# dictionaries for first part of num (before dot)
levels_before_dot = {
    1: '',
    2: 'тысяч',
    3: 'миллион',
    4: 'миллиард',
    5: 'триллион',
    6: 'квадрилион',
    7: 'квинтильон',
    8: 'секстильон',
    9: 'септильон',
    10: 'октальон',
    11: 'нональон',
    12: 'декальон',
    13: 'эндекальон',
    14: 'додекальон',
}
digit_c = {
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
}
digit_b = {
    '1': 'десять',
    '2': 'двадцать',
    '3': 'тридцать',
    '4': 'сорок',
    '5': 'пятьдесят',
    '6': 'шестьдесят',
    '7': 'семьдесят',
    '8': 'восемьдесят',
    '9': 'девяносто',
}
digit_a = {
    '1': 'сто',
    '2': 'двести',
    '3': 'триста',
    '4': 'четыреста',
    '5': 'пятьсот',
    '6': 'шестьсот',
    '7': 'семьсот',
    '8': 'восемьсот',
    '9': 'девятьсот',
}
digit_11_19 = {
    '1': 'одиннадцать',
    '2': 'двенадцать',
    '3': 'тринадцать',
    '4': 'четырнадцать',
    '5': 'пятнадцать',
    '6': 'шестнадцать',
    '7': 'семнадцать',
    '8': 'восемнадцать',
    '9': 'девятнадцать',
}
ending_for_thousand = {
    '1': 'а',
    '2': 'и',
    '3': 'и',
    '4': 'и',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': '',
    '0': '',
}
ending_for_other_levels = {
    '1': '',
    '2': 'а',
    '3': 'а',
    '4': 'а',
    '5': 'ов',
    '6': 'ов',
    '7': 'ов',
    '8': 'ов',
    '9': 'ов',
    '0': 'ов',
}
# dictionaries for second part of num (after dot)
digit_c_after_dot = {
    '1': 'одна',
    '2': 'две',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
}
levels_after_dot = {
    1: 'десят',
    2: 'сот',
    3: 'тысячн',
    4: 'десятитысячн',
    5: 'стотысячн',
    6: 'миллионн',
    7: 'десятимиллионн',
    8: 'стомиллионн',
    9: 'миллиардн',
    10: 'десятимиллиардн',
    11: 'стомиллиардн',
    12: 'триллионн',
    13: 'десятитриллионн',
    14: 'стотриллионн',
    15: 'квадриллионн',
    16: 'десятиквадриллионн',
}
ending_after_dot = {
    '1': 'ая',
    '2': 'ые',
    '3': 'ые',
    '4': 'ые',
    '5': 'ых',
    '6': 'ых',
    '7': 'ых',
    '8': 'ых',
    '9': 'ых',
}

# function counts levels of num ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def lvl_counter(num_in_string):
    if len(num_in_string) / 3 > round(len(num_in_string) / 3):
        levels = round(len(num_in_string) / 3) + 1
    else:
        levels = round(len(num_in_string) / 3)
    return levels

# split num in string to groups by 3 digits of each level and safe it to list 'nums_list' like ['1', '627', '020', ...]+


def split_num_in_string_to_trios(num_in_string):
    level = lvl_counter(num_in_string)
    trios_list = [''] * level
    no = 3
    for digit in range(len(num_in_string)):
        trios_list[level - 1] = num_in_string[len(num_in_string) - digit - 1] \
                                + trios_list[level - 1]
        no -= 1
        if no == 0:
            no = 3
            level -= 1
    return trios_list

# function converts three digits of not last level in to text ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def convert_trio_not_last_lvl(trio):
    trio_in_text = ''
    # not working yet
    return trio_in_text
# function converts to text first part of num (before dot) +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def convert_digits_before_dot(str_before_dot):
    text_before_dot = ''
    if str_before_dot == '0':
        text_before_dot += ' ноль '
    else:
        size_of_num_list = lvl_counter(str_before_dot)
        if size_of_num_list > 16:  # checking of number size
            return 'Слишком большое число для интерпретации!'
        else:
            # split num to groups by 3 digits of each level and safe it to list 'nums_list'
            trios_list = split_num_in_string_to_trios(str_before_dot)

            # convert every three digits in list by level before dot in text
            for level in range(size_of_num_list):

                # copy by tree digits of each level in trio
                trio = ['0', '0', '0', ]
                for digit in range(len(trios_list[level])):
                    trio[2 - digit] = trios_list[level][len(trios_list[level]) - digit - 1]

                # convert any digit it trio to text
                if trio[0] != '0':
                    text_before_dot += ' ' + digit_a[trio[0]]
                if trio[1] == '1' and trio[2] != '0':
                    text_before_dot += ' ' + digit_11_19[trio[2]]
                elif trio[1] != '0':
                    text_before_dot += ' ' + digit_b[trio[1]]
                if trio[1] != '1' and trio[2] != '0':
                    if size_of_num_list - level == 2 and trio[2] == '1':
                        text_before_dot += ' одна'
                    elif size_of_num_list - level == 2 and trio[2] == '2':
                        text_before_dot += ' две'
                    else:
                        text_before_dot += ' ' + digit_c[trio[2]]

                # add name and ending of every level of num
                if trio != ['0', '0', '0']:
                    text_before_dot += ' ' + levels_before_dot[size_of_num_list - level]

                    if size_of_num_list - level == 2 and trio[1] != '1':
                         text_before_dot += ending_for_thousand[trio[2]]
                    if trio[1] != '1' and size_of_num_list - level > 2:
                            text_before_dot += ending_for_other_levels[trio[2]]
                    elif trio[1] == '1' and size_of_num_list - level > 2:
                            text_before_dot += 'ов'

    return text_before_dot

# function converts to text second part of num (after dot) +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def convert_digits_after_dot(str_after_dot):
    str_after_dot = str_after_dot[:4]  # round as you wish
    text_after_dot = ''

    size_of_num_list = lvl_counter(str_after_dot)

    # split result in string in to list 'nums_list' of groups of 3 digits by levels
    trios_list = split_num_in_string_to_trios(str_after_dot)

    # convert every three digits in list by level after dot in text
    for level in range(size_of_num_list):

        # copy by tree digits of each level in trio
        trio = ['0', '0', '0', ]
        for digit in range(len(trios_list[level])):
            trio[2 - digit] = trios_list[level][len(trios_list[level]) - digit - 1]

        # convert any digit it trio to text
        if trio[0] != '0':
            text_after_dot += ' ' + digit_a[trio[0]]
        if trio[1] == '1' and trio[2] != '0':
            text_after_dot += ' ' + digit_11_19[trio[2]]
        elif trio[1] != '0':
            text_after_dot += ' ' + digit_b[trio[1]]
        if trio[1] != '1' and trio[2] != '0':
            if size_of_num_list - level == 2 and trio[2] == '1':
                text_after_dot += ' одна'
            elif size_of_num_list - level == 2 and trio[2] == '2':
                text_after_dot += ' две'
            else:
                text_after_dot += ' ' + digit_c_after_dot[trio[2]]

        # add name and ending of every except last level of num
        if trio != ['0', '0', '0']:
            text_after_dot += ' ' + levels_before_dot[size_of_num_list - level]

            if size_of_num_list - level == 2 and trio[1] != '1':
                text_after_dot += ending_for_thousand[trio[2]]
            if trio[1] != '1' and size_of_num_list - level > 2:
                text_after_dot += ending_for_other_levels[trio[2]]
            elif trio[1] == '1' and size_of_num_list - level > 2:
                text_after_dot += 'ов'

            # add ending for last level digits
            if size_of_num_list - level == 1:
                if trio[1] != '1':
                    text_after_dot += levels_after_dot[len(str_after_dot)] \
                                      + ending_after_dot[trio[2]]
                else:
                    text_after_dot += levels_after_dot[len(str_after_dot)] + 'ых'

    return text_after_dot

# main function to convert num to text +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def num_to_text_converter(num):
    text = ''
    if num < 0:
        text = 'минус'
    num_in_string = str(abs(num))

    # no checking for absent dot needed because num is always float type
    dot_position = num_in_string.find('.')

    # return first part of num (before dot) in text
    text += convert_digits_before_dot(num_in_string[:dot_position])

    # if there is a second part of num (after dot) return it in text
    if num != int(num):
        text += 'и'
        round_text = " (приведено с округлением до 4 заков после запятой)" \
            if len(num_in_string[num_in_string.find('.'):]) > 5 else ''
        text += convert_digits_after_dot(num_in_string[dot_position + 1:]) + round_text
    return text
