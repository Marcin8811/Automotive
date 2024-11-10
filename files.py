# var = input("Напиши что-нибудь: ")
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

# a - это запись новых данных в файл, и помоещение новых данных в конец файла
# w - это также запись новых данных, но с удалением старых данных

# fw = open('doc/file2.txt', 'w')
# fw.write("privet!!!")
# fw.close()

fr = open('doc/file.txt', 'r')
text = fr.read()
fr.close()

print(text)