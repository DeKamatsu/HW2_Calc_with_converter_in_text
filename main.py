# calculator with 4 operations, answer in text
# author: Denis Matveev
# ver.2022.03.06

from num_converter import num_to_text_converter

# function for stop checking +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def stop_checking(txt):
    if txt == 'стоп' or txt == 'stop' or txt == 'Стоп' or txt == 'Stop' or txt == 'СТОП' or txt == 'STOP':
        return True
    return False

# function for num input +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def num_input(txt):
    num_is_digit = False
    while num_is_digit is False:
        try:
            print(f"Введите {txt} число:")
            num = input()
            if stop_checking(num):
                return num
            num = float(num)
            num_is_digit = True
            return num
        except ValueError:
            print("Некорректный формат числа, повторите ввод.")


# main block +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


count = 0
while True:
    operator = ''
    stop = False

    first_num = num_input("первое")  # input first number
    if type(first_num) == str:
        stop = True

    # input operator
    if stop:
        break
    is_operator_ok = False
    while is_operator_ok is False:
        operator = input("Введите операцию (доступны: +, -, *, /):\n")
        if stop_checking(operator):
            stop = True
            break
        elif operator == '+' or operator == '-' or operator == '*' or operator == '/':
            is_operator_ok = True
        else:
            print("Некорректный оператор. Допустимы '+', '-', '*', '/'. Повторите ввод.")

    if stop:
        break
    second_num = num_input("второе")  # input second number
    if type(second_num) == str:
        stop = True
        break

    # Calculation
    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    elif second_num == 0:
        print('Деление на ноль!')
    else:
        result = first_num / second_num

    # output result
    if second_num != 0 or operator != '/':
        result_to_convert = result
        if result == int(result):
            result = int(result)
        if result >= 10000000000000000:
            print("Результат в цифре = ", result)
            print('Слишком большое число для перевода в текст')
        else:
            print("Результат в цифре = ", result)
            print("Результат в тексте = ", num_to_text_converter(result_to_convert))

    count += 1
print(f"Вычисления прерваны. Выполнено {count} рассчетов.")
