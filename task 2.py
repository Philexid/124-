# #criate
# a = ' привет ' # одинарные кавычки
# b = " привет " # Двойные кавычки
# c = " я ' знаю ' Python " # Комбинированные кавычки
# d = ' я " знаю " Python ' # Можно и так
# e = ' я " знаю ' Python " # так нельзя
#
# a = 123 # Целочисленный тип
# a = str(a) # Результат, '123'
# str([1, 1.1, 'a']) # результат, "[1, 1.1, 'a']"
# str(True) # Результат, 'True'
# str(None) # Результат, 'None'
#
# a = 'привет'
# b = 'Иван'
# c = f"{a} я {b}" # привет я Иван
#
# #Retrive
# a = 'привет'
# print(a)
# print('Иван')
#
# a = 'привет'
# a[0] # п
# a[1] # р
# a[2] # и
# a[3] # в
# a[4] # е
# a[5] # т
# a[6] # Ошибка вышли за границы
# a[-1] # т
# a[-2] # е
# a[-3] # в
# a[-4] # и
# a[-5] # р
# a[-6] # п
# a[-7] # Ошибка вышли за границы
#
# #Update
# a = 'бривет'
# a[0] = 'п'
# а = 'привет'
#
# #Delete
# a = 'привет'
# del a [0]
# del a

a = 1, 2, 3
b = str(a)
print(b)
print(type(b))

a = 1, 5.5, "hello"
b = list(a)
print(b)
print(type(b))


a = int(input('ведите целое число:-'))
if a % 2 == 0:
    print(f'Число{a} является чётным')
else:
    print(f'Число{a} является нечётным')