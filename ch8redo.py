#!/usr/bin/env python3


'''def greeter_user():   # 所有函数以'def'开头，空格后为函数名，括号内写函数的参数。
    print("Hello, world ! ")
    
greeter_user() #执行函数。'''

'''def greeter_user(user_name):  #在定义函数的括号内为形参，完成工作所需的一项参数。
    print('Hello ' + user_name.title() + ' !') 
    
greeter_user('noob') #在调用函数的括号内为实参，调用函数时传递给函数的信息。'''

#practice 8-1:

'''def display_message():
    print('this chapter will cover function!')
display_message()'''

#practice 8-2:

'''def favorite_book(title):
    print('one of my favorite books is ' + title + '.')

favorite_book('Alice in Wonderland')'''


'''传递实参
1. 位置实参：要求形参和实参的顺序相同
2. 关键字实参：每个实参由变量名和值组成
'''

'''def describe_pet(animal_type, pet_name):
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '\'s name is ' +
        pet_name.title() + '.')
        
describe_pet('hamster','harry')'''

'''def describe_pet(animal_type,pet_name):
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '\'s name is ' +
        pet_name.title() + '.')

describe_pet(pet_name = 'harry', animal_type = 'hamster')'''

'''def describe_pet(pet_name, animal_type = 'dog'):
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '\'s name is ' +
        pet_name.title() + '.')

describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(pet_name = 'harry')'''


#practice 8-3:

'''def make_shirt(shirt_size, shirt_pattern):
    print('\nThe shirt your ordered is in ' + shirt_size + ' size.')
    print('\nThe pattern on the shirt is ' + shirt_pattern)
    
make_shirt(shirt_size = 'medium', shirt_pattern = 'huajilian')'''


#practice 8-4:

'''def make_shirt(shirt_size, shirt_pattern = 'I Love Python'):
    print('\nThe shirt your ordered is in ' + shirt_size + ' size.')
    print('\nThe pattern on the shirt is \'' + shirt_pattern + '\'.')
    print('-------------------------------------------------------')


make_shirt(shirt_size = 'large')
make_shirt(shirt_size = 'medium')
make_shirt(shirt_size = 'medium', shirt_pattern = 'huajilian')'''


#practice 8-5:

'''def describe_city(city_name, country = 'Canada'):
    print(city_name.title() + ' is located in ' + country.title() + '.')
    
describe_city('Vancouver')
describe_city('Toronto')
describe_city('Beijing', 'China')'''


'''def formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = formatted_name('hang','su') #使用返回值(return)时，需要提供一个变量来存储这个返回值
print(musician)'''

#让实参变成可选的，这样再有必要的时候才需要提供信息

'''def formatted_name(first_name, last_name, middle_name = ''):
    if not middle_name:
        full_name = first_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        
    return full_name.title()
    
user_name = formatted_name('hang', 'su')
print(user_name)
user_name = formatted_name('tong', 'liu', 'peter')
print(user_name)'''


#返回字典

'''def build_person(first_name, last_name, age = ''):
    person = {'first':first_name.title(),'last':last_name.title()}
    if age:
        person['age'] = age
    return person
    
var = build_person('hang','su',27)
print(var)'''


'''def get_formatted_name(first_name, last_name, age = ''):

    full_name = first_name + ' ' + last_name
    return full_name.title()
    
while True:
    print('\nPlease tell me your name:')
    f_name = input('first name: ')
    if f_name == 'q':
        break
    
    l_name = input('last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')'''


#practice 8-6:

'''def city_country(city_name,country):
    info = '"' + city_name.title() + ', '+ country.title() + '\"'
    return info

info_entry = city_country('beijing','china') 
print(info_entry)

info_entry = city_country('tokyo','japan') 
print(info_entry)
    
info_entry = city_country('vancouver','canada') 
print(info_entry)'''

#practice 8-7:

'''def make_album(singer_name, album_name, song_number=''):
    if song_number:
        info = {'singer':singer_name,'album':album_name,'# of songs':song_number}
    else:
        info = {'singer':singer_name,'album':album_name}
    return info
    
newalbum = make_album('jay', 'fantasy',10)
print(newalbum)

newalbum = make_album('a', 'b')
print(newalbum)

newalbum = make_album('c', 'd')
print(newalbum)'''

#practice 8-8:

'''def make_album(singer_name, album_name, song_number=''):
    if song_number:
        info = {'singer':singer_name,'album':album_name,'# of songs':song_number}
    else:
        info = {'singer':singer_name,'album':album_name}
    return info

while True:

    singer_name_input = input('what\'s the singer\'s name?\n')
    album_name_input = input('what\'s the album\'s name?\n')
    song_number_input = int(input('how many songs in the album?\n'))
    
    newalbum = make_album(singer_name_input, album_name_input, song_number_input)
    print(newalbum)


    program = input('input \'q \'to quit this program.')
    if program == 'q':
        break'''
        
        
#8.4传递列表

'''def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)
        
usernames = ['hannah','ty','margot']
greet_users(usernames)'''


'''unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print('printing model ' + current_designs + '....')
    completed_models.append(current_designs)

print('\nThe following design will be completed:')
for completed_model in completed_models:
    print(completed_model)'''


'''def print_models(unprinted_designs, completed_models):
    
    while unprinted_designs:

        current_designs = unprinted_designs.pop()
        print('printing model ' + current_designs + '....')
        completed_models.append(current_designs)


def finished(completed_models):
    print('\nThe following design will be completed:')
    for completed_model in completed_models:
        print(completed_model)
    

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
finished(completed_models)
print(unprinted_designs)'''


#practice 8-9,10,11:

'''    print('the magicians we have here are ')
    for name in names:
        print('\n' + name)


def make_great(names):
    new_names = []
    
    while names: 
        change_name = names.pop()
        x = change_name + ' the Great'
        new_names.append(x)
    
    for great_magician in new_names:
        names.append(great_magician)
        print(great_magician)

    
names = ['a','b','c']
show_magician(names)

#print('\n')
make_great(names[:]) #禁止修改列表符号参数，在引用修改列表的的函数时使用
show_magician(names)'''


'''def make_pizza(size, *toppings):
    for topping in toppings:
        print(str(size) + ' ' + topping)
    
make_pizza(12, 'a')
make_pizza(16, 'b','c')'''


def build_profile(first, last, **user_info):
    person = {}
    person['first_name'] = first
    person['last_name'] = last
    for key, value in user_info.items():
        person[key] = value
    return person
    
user_profile = build_profile('a','b',place='beijing')
print(user_profile)


























