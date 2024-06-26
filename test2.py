#CREATE list
a = []
b = list()

a = [1, 1.1, 'a', [1], (1, 1.1), (1, 2), {'a': 1}, None, True]
# Список в котором: целое;вещественное;строковое;другой список;кортеж;множество;словарь;пустой тип;булевый тип.

а = [] # Пустой список
b = list() # Пустой список

a = (1, 2.1, 3)
# Раньше я был кортежем list(a) # [1, 2.1, 3], но 'а' остался кортежем >>> b = list('abc') # ['a', 'b', 'c']

#RETRIVE list

a = [1, 1.1, 'a']
print(a) # [1, 1.1, 'a']
print([1, 1.1, 'a']) # [1, 1.1, 'a']

a = [1, 1.1, 'a']
a[0] #1
a[1] #1.1
a[2] # 'a'
а[3] # Ошибка, вышли за границы
2
a[-1] # 'a'
a[-2] #1.1
[-3] #1
a[-4] #Ошибка, вышли за границы

a = [1, 2, 3]
a.index(3)
#2. Возвращает индекс, где передаваемое значение стоит в списке. В примере вернётся 2, так как значение 3 в списке стоит на 2-ом индексе.

#UPDATE list

a = [1, 1.1, 'a']
a[0] = 'a' # Теперь 'а' равно ['a', 1.1, 'a']
a[1] = '6' # Теперь 'а' равно ['а', 'б', 'а']
a[-1] = 'B' # Теперь 'а' равно ['а', 'б', 'в']
a = [1, 2, 3] # Теперь 'а' равно [1, 2, 3]

a = [1, 2, 3]
a.append(4) # Добавляет значение (объект) в конец списка. Добавляет только один объект или значение. Теперь "а" [1, 2, 3, 4
a.append(['a', 'b']) # Teneерь "а" 1, 2, 3, 4, ['a', 'b']]. Не забываем, что методы в списке изменяют значения и структуру в самом списке.
a = [1, 2, 3]
a.insert(0, 4) # Добавляет значение (объект), что стоит на втором месте (4) на место под индексом, что стоит на первом вместе (0). В конкретном примере добавит 4 на 10-ой индекс, т.е. вначало. Теперь "а" [4, 1, 2, 3]
a = [1,2,3]
a.insert(3, 4) # В конкретном примере добавит 4 на 3-ий индекс, т.е. вконец. Теперь a [1, 2, 3, 4].
a = [1, 2, 3]
a.insert(-1, 4) # Кажется, что здесь должно значение 4 добавиться в конец, но на самом деле 4 встанет в предпоследнее место. Тепер "a" [1, 2, 4, 3].
a = [1, 2, 3]
a.extend([4, 5, 6]) # Добавляет данные в список поэлементно. Теперь "а" [1, 2, 3, 4, 5, 6)

#DELETE list

a = [1, 1.1, 'a']
del a[0] # Теперь 'а' равно [1.1, 'a'] >>> del a[-1] # Теперь 'а' равно [1.1]
del a[-1] # Теперь 'а' равно
del a # Полное удаление переменной "а"

a = [1, 2, 3]
a.clear() # Полностью очищает список, превращая его в пустой список. Теперь "а"
a = [1, 2, 3]

# методы

help(list) # Информация о списках > a = [1, 1, 3, 1]
a.count(1) # 3. Возвращает сколько раз в списке встретилось передаваемое значение. В примере вернётся 3, так как в списке три единицы.
a = [1, 2, 3]
a.copy() # [1, 2, 3]. Возвращает копию списка. Это удобно, чтобы скопировать данные в новую переменную и изменять значения уже в новой переменной, чтобы значения в старой переменной не изменились.
a = [1, 2, 3]
a.reverse() # Полностью переворачивает список. Теперь "а" [3, 2, 1]
a = [2, 1, 3]
a.sort() # Сортирует значения в списке в порядке ВОЗРАСТАНИЯ. Теперь "а" [1, 2, 3] >
a = [2, 1, 3]
a.sort(reverse=True) # Сортирует значения в списке в порядке УБЫВАНИЯ. Теперь "а" [3, 2, 1]