# Задача 1
empty_tuple = () # Пустой кортеж
tuple_with_one_item = (1,) # кортеж из одного элемента
tuple_ = (1, 2, "str")
print("Содержимое переменной empty_tuple:", empty_tuple,
type(empty_tuple))
print("Содержимое переменной tuple_with_one_item:",
tuple_with_one_item, type(tuple_with_one_item))
print("Содержимое переменной tuple_:", tuple_, type(tuple_))
list_ = [] # Пустой список
chars_list = ["a", "b", "c"]
print("Содержимое переменной list_:", list_, type(list_))
print("Содержимое переменной chars_list:", chars_list,
type(chars_list))
empty_string = "" # Пустая строка
str_ = "test" # Строковый тип данных
print("Содержимое переменной empty_string:", empty_string,
type(empty_string))
print("Содержимое переменной str_:", str_, type(str_))
empty_set = set() # Пустое множество
set_ = {3, 2, 1, 1} # Множество содержит в себе только уникальные элементы
print("Содержимое переменной empty_set:", empty_set,
type(empty_set))
print("Содержимое переменной set_:", set_, type(set_))
empty_dict = {} # Пустой словарь
dict_ = {"Имя": "Ваше имя",
 "Фамилия": "Ваша фамилия",
 "Возраст": 18,
 "Возраст": 20,}# Словарь хранит пары ключ-значение. Ключи должны быть уникальными значениями
print("Содержимое переменной empty_dict:", empty_dict,
type(empty_dict))
print("Содержимое переменной dict_:", dict_, type(dict_))

student_scores = {
 "Маша": 85,
 "Саша": 92,
 "Петя": 78
}
print(student_scores["Маша"]) # Выводит 85
print(student_scores["Саша"]) # Выводит 9
# Задача 1.1
list_players = ["Маша", "Петя", "Саша", "Оля",
"Кирилл"]
last_player = list_players[-1]
reestr = {"Первый участник": list_players[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

shopping_list = ["яблоко", "молоко", "хлеб", "яблоко",
"масло", "яйца", "молоко"]
unique_items = set(shopping_list)
print("Количество уникальных товаров:", len(unique_items))

# Задача 1.2
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
print(seasons_dict)
# задача 2
list_players = ["Маша", "Петя", "Саша","Оля", "Кирилл"]
last_player = list_players[-1]
reestr = {"Первый участник": list_players[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

list_participants = ["Орлов", "Петров", "Иванов", "Сидоров", "Васильев", "Черепахин"]
last_player = list_participants[-1]
reestr = {"Первый участник": list_participants[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

sps_Book=["Дубровский", "Горе от ума", "Кавказский пленник", "Хамелеон","Ревизор", "Гранатовый браслет"]
last_Book = sps_Book[-1]
reestr = {"Первая книга": sps_Book[0]}
print("Последния книга:", last_Book)
print("Последния книга:", reestr["Первая книга"])

shopping_list = ["Палатка", "Спальник", "Котелок", "Тренога", "Рюкзак", "Спальник","Рюкзак", "Термос", "Миска", "Ветровка", "Коврик" ]
unique_items = set(shopping_list)
print("Количество уникальных товаров:", len(unique_items))