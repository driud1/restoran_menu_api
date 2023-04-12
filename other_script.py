# import some_script
#
#
# def foo(a):
#     print(locals())
#     print(globals())
#     return a ** -6
#
#
# print(foo(56))
#
# x = some_script.foo(5)
#
# if __name__ == '__main__':
#     for i in range(10, -1, -1):
#         print(i)
#
#     print(x)
#
#     print(foo(4))




names = ["alan", "dmitri", "sasha"] # список из которого мы записываем имена в каждую отдельную отдельную строку
# и выводим их

# file = open("names.txt", "w") # создаем и записываем файл
#
# for i in names: # цикл записывает каждое имя в отдельную строку
#     file.write(i + "\n")
#
# file.close() # закрываем файл

with open("names.txt", "w") as file:  #открывает файл для записи
    for i in names: # цикл записывает каждое имя в отдельную строку
        file.write(i + '\n')
    # close можно не использовать так как при выходе из блока with файл закрывается автоматически

# n_file = open("names.txt", "r") # открывает файл для чтения
#
# file_lines = n_file.readlines() # Считывает из файла одну строку и возвращает её.
# print(file_lines) # выводит полученную строку
#
# for i in n_file.readlines(): #считывает количество строк
#     print(i) #
#
# n_file.close()

with open("names.txt", "r") as file:  # Открывает для чтения существующий файл.
    for i in file.readlines(): # возвращает список строк
        print(i, end='') # выводит каждое имя из списка в новую строку

