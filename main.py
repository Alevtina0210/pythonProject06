immutable_var = (5, 10, 15, 'element', '2,5', False)
print(immutable_var)
# immutable_var[0] = 3
# print(immutable_var), кортеж нельзя изменить, т.к. в нем хранится ссылка на список, а не сам список.
# кортеж - неизменяемая коллекция, не поддерживающая обращение по элементам
mutable_list = ['Moscow', 'Togliatty', 'Saratov', 1, 2, '0,1']
print(mutable_list)
mutable_list.extend('Voronezh')
print(mutable_list)
mutable_list[0] = 'Penza'
print(mutable_list)
