first_name = "Ivan"
last_name = "Ivanov"
a = '{} {}'
result = a.format(first_name, last_name)
print("Меня зовут: " + result)

result = f'Меня зовут: {first_name} {last_name}'
print(result)