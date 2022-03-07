# calculator with 4 operations, answer in text
# author: Denis Matveev
# ver.2022.03.06

from recognizer import digital_recognizer

# function for num input
def num_input (txt):
    num_is_digit = False
    while num_is_digit is False:
        try:
            print(f"Введите {txt} число:")
            num = float(input())
            num_is_digit = True
            return num
        except ValueError:
            print ("Некорректный формат числа, повторите ввод.")


# input first number
operator = ''
first_num = num_input("первое")

# input operator
is_operator_ok = False
while is_operator_ok is False:
    operator = input("Введите операцию:\n")
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        is_operator_ok = True
    else:
        print("Некорректный оператор. Допустимы '+', '-', '*', '/'. Повторите ввод.")

# input second number
second_num = num_input("второе")

# Calculation
if operator == '+':
    result = first_num + second_num
elif operator == '-':
    result = first_num - second_num
elif operator == '*':
    result = first_num * second_num
elif second_num == 0:
    print ('Деление на ноль!')
else:
    result = first_num / second_num


# recognize digital result to text
if second_num != 0 and operator != '/':

    text_result = (digital_recognizer(result))

    # digital output
    if result == int(result):
       result = int(result)
    print("Результат = ", result)

    #text output
    print("Результат = ", text_result)



