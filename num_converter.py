# converter of num to text
# author: Denis Matveev
# ver.2022.03.13

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
digit_c_male = {
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
digit_c_float_before_dot = {
    '1': 'одна целая',
    '2': 'две целых',
    '3': 'три целых',
    '4': 'четыре целых',
    '5': 'пять целых',
    '6': 'шесть целых',
    '7': 'семь целых',
    '8': 'восемь целых',
    '9': 'девять целых',
}
digit_c_female = {
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

# split num in string to groups by 3 digits of each level and safe it to list 'nums_list' like ['001', '627', ...]++++++


def split_num_in_string_to_trios(num_in_string):
    level = lvl_counter(num_in_string)
    trios_in_list = [''] * level
    no = 3
    for digit in range(len(num_in_string)):
        trios_in_list[level - 1] = num_in_string[len(num_in_string) - digit - 1] + trios_in_list[level - 1]
        no -= 1
        if no == 0:
            no = 3
            level -= 1
    absent_digit = 3 - len(trios_in_list[0])  # count quantity of digits of highest level of num^ 1, 2 or 3 ++++++++++++
    trios_in_list[0] = '0' * absent_digit + trios_in_list[0]  # add 0 to replace absent digits on highest level of num +
    return trios_in_list

# function converts three digits of each level in to text ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def convert_3_digits_to_text(trio, list_size, level, is_firs_part_of_num, integer):
    for digit in range(len(trio)):
        trio_in_text = ''
        # cases for choosing a correct dictionary for UNITS level:
        # 1) not units & not thousands levels OR units levels before dot for integer num - typical case
        # 2) units levels before dot for float num except 11-19
        # 3) units levels after dot & thousands level - female

        if trio[2] != '0' and trio[1] != '1':
            if list_size - level > 2 or (list_size - level == 1 and is_firs_part_of_num and integer):  # 1) typical case
                trio_in_text = digit_c_male[trio[2]] + ' ' + trio_in_text
            elif list_size - level == 1 and is_firs_part_of_num and integer is False:  # 2) before dot in float num ++++
                trio_in_text = digit_c_float_before_dot[trio[2]] + ' ' + trio_in_text
            elif list_size - level == 2 or is_firs_part_of_num is False:   # 3) thousands OR unit after dot in float num
                trio_in_text = digit_c_female[trio[2]] + ' ' + trio_in_text

        # convert TENS it trio to text
        if trio[1] == '1' and trio[2] != '0':
            if list_size - level == 1 and is_firs_part_of_num and integer is False:  # add for float num before dot
                trio_in_text = 'целых '
            trio_in_text = digit_11_19[trio[2]] + ' ' + trio_in_text
        elif trio[1] != '0':
            trio_in_text = digit_b[trio[1]] + ' ' + trio_in_text

        # convert HUNDREDS it trio to text
        if trio[0] != '0':
            trio_in_text = digit_a[trio[0]] + ' ' + trio_in_text
    return trio_in_text

# function add endings to each level trios in text +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def add_lvl_name_with_ending(trio, list_size, level, is_firs_part_of_num, length_after_dot):
    # cases for choosing a correct dictionary of ENDINGS to differ levels:
    # 1) not units & not thousands levels & not 11-19
    # 2) 11-19 not units or not thousands levels
    # 3) thousands level: 3.1) not 11-19, 3.2) 11-19
    # 4) units levels after dot: 4.0) zero after dot, 4.1) not 11-19, 4.2) 11-19
    if float(trio) == 0:
        name_with_ending = ''
    else:
        name_with_ending = levels_before_dot[list_size - level]
        if list_size - level > 2 and trio[1] != '1':  # 1) not units & not thousands levels & not 11-19
            name_with_ending += ending_for_other_levels[trio[2]] + ' '
        elif list_size - level > 2 and trio[1] == '1':  # 2) 11-19 not units or not thousands levels
            name_with_ending += 'ов '
        elif list_size - level == 2 and trio[1] != '1':  # 3.1) thousands level, not 11-19
            name_with_ending += ending_for_thousand[trio[2]] + ' '
        elif list_size - level == 2 and trio[1] == '1':  # 3.2) thousands level, 11-19
            name_with_ending += ' '
        elif list_size - level == 1 and is_firs_part_of_num is False:  # 4) units levels after dot:
            if float(trio) == 0:  # 4.0) zero after dot
                name_with_ending = ''
            elif trio[1] != '1':  # 4.1) not 11-19
                name_with_ending = levels_after_dot[length_after_dot] + ending_after_dot[trio[2]] + ' '
            else:  # 4.2) 11-19
                name_with_ending = levels_after_dot[length_after_dot] + 'ых '
    return name_with_ending

# function converts to text first part of num (before dot) +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def convert_digits_before_dot(str_before_dot, integer):
    text_before_dot = ''
    if str_before_dot == '0':  # checking for zero value
        text_before_dot += 'ноль '

    quantity_of_levels = lvl_counter(str_before_dot)  # checking of number size
    if quantity_of_levels > 16:
        return 'Слишком большое число для интерпретации!'

    else:
        # split num to groups by 3 digits of each level and safe it to list 'nums_list'
        trios_list = split_num_in_string_to_trios(str_before_dot)

        for level in range(quantity_of_levels):
            # convert every three digits of each level of num before dot in text
            text_before_dot += convert_3_digits_to_text(trio=trios_list[level]
                                                        , list_size=quantity_of_levels
                                                        , level=level
                                                        , is_firs_part_of_num=True
                                                        , integer=integer)
            # add name and ending of every level of num
            text_before_dot += add_lvl_name_with_ending(trio=trios_list[level]
                                                        , list_size=quantity_of_levels
                                                        , level=level
                                                        , is_firs_part_of_num=True
                                                        , length_after_dot=0)
    if integer is False and trios_list[len(trios_list) - 1][2:] == '0':  # check float value for 0 OR x*10 num
        text_before_dot += 'целых '
    return text_before_dot

# function converts to text second part of num (after dot) +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def convert_digits_after_dot(str_after_dot):
    text_after_dot = ''
    quantity_of_levels = lvl_counter(str_after_dot)

    # split num to groups by 3 digits of each level and safe it to list 'nums_list'
    trios_list = split_num_in_string_to_trios(str_after_dot)

    for level in range(quantity_of_levels):
        # convert every three digits of each level of num after dot in text
        text_after_dot += convert_3_digits_to_text(trio=trios_list[level]
                                                   , list_size=quantity_of_levels
                                                   , level=level
                                                   , is_firs_part_of_num=False
                                                   , integer=False)
        # add name and ending of every level of num
        text_after_dot += add_lvl_name_with_ending(trio=trios_list[level]
                                                   , list_size=quantity_of_levels
                                                   , level=level
                                                   , is_firs_part_of_num=False
                                                   , length_after_dot=len(str_after_dot))
    return text_after_dot

# main function to convert num to text +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def num_to_text_converter(num):
    text = ''
    if num < 0:
        text = 'минус '
    num_round = round(num, 4)  # round as you wish
    no_round = num == num_round  # check if num is rounded
    num_in_string = str(abs(num_round))
    dot_position = num_in_string.find('.')  # no checking for absent dot needed because num is always float type
    # check if rounded num is integer
    zero_after_dot = len(num_in_string[dot_position + 1:]) < 2 and num_in_string[dot_position + 1:] == '0'

    text += convert_digits_before_dot(str_before_dot=num_in_string[:dot_position]
                                      , integer=zero_after_dot)  # return 1-st part of num (before dot) in text

    if zero_after_dot is False:  # if there is a 2-nd part of num (after dot) return it in text
        text += convert_digits_after_dot(num_in_string[dot_position + 1:])
    if no_round is False:
        text += "(приведено с округлением до 4 заков после запятой)"
    return text
