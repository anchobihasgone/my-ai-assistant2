#1
# techno = ['ИИ', 'Геймдев', 'Бэкенд']
# print(techno)
# print(techno[0])
# print(techno[-1])


#2
# marks = [2, 3, 4, 5]
# print(marks[1])
# print(len(marks))


#3
# subs = ['Maths', 'Geography', 'English', 'Biology']
# subs[2] = 'Geometry'
# print(subs)


#4
# prog_lang = ['C', 'C#']
# prog_lang.append('C++')
# print(prog_lang)


#5
# prog = ['Python', 'C++']
# prog.insert(1, "Java")
# print(prog)


#6
# prog = ['Python', 'Java', 'C++', 'C#', 'C']
# prog.remove("Python")
# prog.pop(0)
# print(prog)


#7
# techno = ['Бэкенд', 'ИИ', 'Фронтенд', 'Дизайн', 'Геймдев']
# n = input('Введите название технологиии: ')

# if n in techno:
#     print('Эта технология есть в списке')
# else:
#     print('Эта технологии нет в списке')


#8
# extension = ['.txt', '.csv', '.json']
# user = input('Введите название расширения: ')
# if user in extension:
#     print('Это расширение разрешенно')
# else:
#     print('Это расширение не разрешенно')


#9
# print('---------------     КАРТОЧКА СТУДЕНТА     ---------------')
# dict = {
#     'name': '',
#     'group': '', 
#     'age': 0
# }
# u_name = input('Введите имя: ')
# u_group = input('Введите название группы: ')
# u_age = int(input('Введите возраст: '))
# dict['age'] = u_age
# dict['group'] = u_group
# dict['name'] = u_name
# print(dict)


#10
# print('---------------     КАРТОЧКА СТУДЕНТА     ---------------')
# dict = {
#     'name': '',
#     'group': '', 
#     'age': 0
# }
# u_name = input('Введите имя: ')
# u_group = input('Введите название группы: ')
# u_age = int(input('Введите возраст: '))
# dict['age'] = u_age
# dict['group'] = u_group
# dict['name'] = u_name

# print(dict)

# dict['age'] = 19
# dict['speciality'] = ''
# u_speciality = input('Введите специальность: ')
# dict['speciality'] = u_speciality

# print(dict)


#11
# dic = {
#     'name': 'Анна',
#     'age': 18,
# }

# print(dic)

# dic['city'] = 'Москва'
# print(dic)
# dic.pop('city')
# print(dic)


#12

# name = input("Введите имя: ")
# group = input("Введите группу: ")
# age = int(input("Введите возраст: "))
# speciality = input("Введите специальность: ")

# student = {
# "name": name,
# "group": group,
# "age": age,
# "speciality": speciality
# }

# print(student)


#13
# name = input("Введите имя: ")
# group = input("Введите группу: ")
# age = int(input("Введите возраст: "))
# speciality = input("Введите специальность: ")

# dict = {
#     "name": name,
#     "group": group,
#     "age": age,
#     "speciality": speciality
# }

# new_group = input("Введите новую группу: ")
# dict["group"] = new_group
# print(dict)


#14
# dict = {
# "name": "Анна",
# "group": "1ИИ-1-11",
# "skills": ["Python", "Git", "AI"]
# }
# print(dict["name"])
# print(dict["skills"])
# print(dict["skills"][0])
# print(dict["skills"][-1])


#15
# dict = {
#     "name": "Анна",
#     "group": "1ИИ-1-11",
#     "skills": ["Python", "Git", "AI"]
# }

# dict["skills"].append("Linux")

# print(dict)

#16
# languages = ["Python", "Java", "C++"]
# print(languages[2])
# languages.append("Go")
# languages.remove("Java")
# print(languages)


#17
# dict = {
#     "name": "Анна",
#     "age": 18,
#     "group": "1ИИ-1-11"
# } 

# print(dict["name"])
# dict["age"] = 19
# dict["city"] = ("Москва")
# print(dict)


#Уровень 8. Предскажи результат
# items = ["A", "B", "C"]
# print(items[1])
# Мой прогноз: B

# items = ["A", "B"]
# items.append("C")
# print(len(items))
# Мой прогноз: 3

# items = [10, 20, 30]
# items[0] = 99
# print(items)
# Мой прогноз: [99, 20, 30]

# student = {"name": "Ира", "age": 18}
# print(student["name"])
# Мой прогноз: Ира

# student = {"name": "Ира"}
# student["group"] = "1ИИ"
# print(len(student))
# Мой прогноз: 2


#18
# list = ['Git', 'Vscode', 'Pycharm', 'InteliJ IDEA']
# user = input("Введите название инструмента: ")
# if user in list:
#     print('Этот инструмент уже есть в списке!')
# else:
#     print('Такого инструмента нет! Добавляю в список...')
#     list.append(user)

# print(list)


#19
# proj_name = input('Введите название проекта: ')
# user_name = input('Введите имя автора проекта: ')
# numb_of_parts = int(input('Введите количество участников: '))
# proj_status = input('Введите статус проекта: ')

# project = {
#     'name': proj_name,
#     'user': user_name,
#     'participants': numb_of_parts,
#     'status': proj_status
# }

# print('-------КАРТОЧКА ПРОЕКТА-------')

# print('Название проекта: ', project['name'])
# print('Имя автора: ', project['user'])
# print('Количество участников: ', project['participants'])
# print('Статус проекта: ', project['status'])


#20
# proj_name = input('Введите название проекта: ')
# user_name = input('Введите имя автора проекта: ')
# numb_of_parts = int(input('Введите количество участников: '))
# proj_status = input('Введите статус проекта: ')

# project = {
#     'name': proj_name,
#     'user': user_name,
#     'participants': numb_of_parts,
#     'status': proj_status
# }

# project['technologies'] = ['Git', 'Vscode', 'Pycharm']


# print('Название проекта: ', project['name'])
# print('Технологии: ', project['technologies'])
# print('Первая технология: ', project['technologies'][0])


#21
title = input("Название проекта: ")
author = input("Имя автора: ")
group = input("Группа: ")
members = int(input("Количество участников: "))
status = input("Статус проекта: ")

technologies = ["Python", "SQL", "Docker"]

project = {
    "title": title,
    "author": author,
    "group": group,
    "members": members,
    "status": status,
    "technologies": technologies
}

print(project["title"])
print(project["author"])
print(project["members"])
print(project["technologies"])
print(project["technologies"][0])
print(project["technologies"][-1])
print(len(project["technologies"]))

new_tech = input("Введите ещё одну технологию: ")
project["technologies"].append(new_tech)

check_tech = input("Введите технологию для проверки: ")
if check_tech in project["technologies"]:
    print("Есть в списке")
else:
    print("Нет в списке")

new_status = input("Введите новый статус: ")
project["status"] = new_status

print(project)
