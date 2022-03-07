# converter of num to text
# author: Denis Matveev
# ver.2022.03.06

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
    1: 'а',
    2: 'и',
    3: 'и',
    4: 'и',
    5: '',
    6: '',
    7: '',
    8: '',
    9: '',
    0: '',
}
ending_for_other_levels = {
    1: '',
    2: 'а',
    3: 'а',
    4: 'а',
    5: 'ов',
    6: 'ов',
    7: 'ов',
    8: 'ов',
    9: 'ов',
    0: 'ов',
}
# dictionaries for second part of num (after dot)
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
    '2-4': 'ые',
    '5-0': 'ых',
}

# function converts in text first part of result (before dot)
def convert_digit_before_dot(str_before_dot):
    text_result_before_dot = ''

    # checking of number size
    if len(str_before_dot) / 3 > round(len(str_before_dot) / 3):
        size_of_num_list = round(len(str_before_dot) / 3) + 1
    else:
        size_of_num_list = round(len(str_before_dot) / 3)

    if size_of_num_list > 7:
        return('Слишком большое число для интерпретации!')

    # split result in string in to list 'nums_list' of groups of 3 digits by levels
    nums_list = [''] * size_of_num_list
    level = size_of_num_list
    no = 3
    for digit in range(len(str_before_dot)):
        nums_list[level - 1] = str_before_dot[len(str_before_dot) - digit - 1] \
                               + nums_list[level - 1]
        no -= 1
        if no == 0:
            no = 3
            level -= 1

    # convert every three digits in list by level before dot in text
    for level in range(size_of_num_list):
        trio = ['0', '0', '0', ]
        for digit in range(len(nums_list[level])):
            trio[2 - digit] = nums_list[level][len(nums_list[level]) - digit - 1]
        if trio[0] != '0':
            text_result_before_dot += ' ' + digit_a[trio[0]]
        if trio[1] == '1' and trio[2] != '0':
            text_result_before_dot += ' ' + digit_11_19[trio[2]]
        elif trio[1] != '0':
            text_result_before_dot += ' ' + digit_b[trio[1]]
        if trio[1] != '1' and trio[2] != '0':
            text_result_before_dot += ' ' + digit_c[trio[2]]
        if level == size_of_num_list - 1 and trio[0] == '0' and trio[1] == '0' and trio[2] == '0':
            text_result_before_dot += ' ноль'

        # add name of every level of num
        text_result_before_dot += ' ' + levels_before_dot[size_of_num_list - level]
        if size_of_num_list - level == 2 and trio[1] != 1:
            text_result_before_dot += ending_for_thousand[int(trio[2])]
        elif trio[1] != 1 and size_of_num_list - level != 1:
                text_result_before_dot += ending_for_other_levels[int(trio[2])]
        elif size_of_num_list - level != 1:
                text_result_before_dot += 'ов'

    return (text_result_before_dot)

# function converts in text second part of result (after dot)
def convert_digit_after_dot(str_after_dot):

    return (text_result_after_dot)

# main function to recognize num in text
def digital_recognizer (digital_result):
    result_in_string = str(digital_result)
    length_all = len(result_in_string)

#    print("It's ok. all Length = ", length_all) # ------------------

    # no checking for absent dot because result is float type
    dot_position = result_in_string.find('.')
    digits_after_dot = length_all - dot_position - 1

#    print("It's ok. Length before = ", dot_position) # ---------------

    # return first part of result (before dot) in text
    text_result = convert_digit_before_dot(result_in_string[:dot_position])

#    print("It's ok. text_result = ", text_result) # ---------------

    # if there is a second part of result (after dot) return it in text
    if digital_result != int(digital_result):
        text_result =+ " целых "
        text_result =+ convert_digit_after_dot(result_in_string[digits_before_dot + 1:])
    return(text_result)


