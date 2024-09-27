var_1 = 100 # глобальная переменная
var_2 = 20 # глобальная переменная
print(var_1, var_2)

def sum():
    result = var_1 + var_2
    print(result)

def sub():
    var_2 = 30
    result = var_1 - var_2
    print(result)
sum()
sub()