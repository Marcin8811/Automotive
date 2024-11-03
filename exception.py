a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение: "))

try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print("На 0 делить нельзя.")
print("Результат вычитания : " + str(result))

result_2 = int(a + b)
print("Результат сложения : " + str(result_2))
# ZeroDivisionError