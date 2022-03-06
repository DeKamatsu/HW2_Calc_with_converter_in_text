# calculator with 4 operations, answer in text

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
first_num, second_num = 0, 0
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
else:
    if operator == '-':
        result = first_num - second_num
    else:
        if operator == '*':
            result = first_num * second_num
        else:
            result = first_num / second_num
print("Результат = ", result)



