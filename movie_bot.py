import time, random, os

films = ['Человек-паук: Нет пути домой', 'Джентльмены', 'Выживший', '1+1', 'Гнев человеческий', 'Веном 2', 'Мстители: Финал', 'Собачья жизнь 2', 'Зеленая книга', 'Движение вверх', 'Бесконечный поезд', 'Кожа, в которой я живу', 'Операция "Фортуна"', 'Дюна: Часть вторая', 'Алиса в Стране чудес', 'Миа и белый лев', 'Солнцепек', 'Гнев человечесткий', 'Хатико', 'Мастер и Маргарита', 'Холоп 2', 'Бременские музыканты', 'Воздух', 'Аквамен и потерянное цартсво', 'По щучьему велению', 'Вонка', 'Три богатыря и Пуп Земли']
list_f = 0
delete_film = 0
add_film_counter = 0
favorit_film = 0
favorit_films_list = []
viewed_films = 0
achievement_counter = 0
achievement = []
viewed_films_list = []
delete_films_list = []
append_films = []
money = 0
money_egg = False
expansion_of_the_territory = False
expansion = False
moon = False
smile_list = ['😃', '😄', '😁', '😆', '😊', '🙂', '🙃', '😋', '😛', '😝', '😜', '🤨', '🤩', '🤗', '🤔', '🤭', '🤫', '😎']

print(10 * '=' + 'Vox' + '=' * 10)
print('Привет, меня зовут Vox👋 \nЯ бот по фильмам')
time.sleep(1)

name = input('Как тебя зовут? ')
print(f'Приятно познакомится {name}!😉')

while True:
    print()

    if list_f == 0:
        q_list = input('Показать список команд?🤨 ')
        q_list.lower()

        if q_list == 'да' or q_list == 'давай':
            print('''
            Список команд:
                  ⚫️ Команды (показывает список команд)
                  ⚫️ Список фильмов (показывает список фильмов)
                  ⚫️ Добавить фильм (добавляет в список фильм)
                  ⚫️ Удалить фильм (удаляет фильм из списка фильмов)
                  ⚫️ Порекомендуй фильм (бот рекомендует фильм)
                  ⚫️ Количество фильмов (показывает количество фильмов)
                  ⚫️ Добавить просмотренный фильм (добавляет в фильм в "Просмотренное")
                  ⚫️ Список просмотренных (показывает список просмотренных фильмов)
                  ⚫️ Количество просмотренных (показывает число просмотренных фильмов)
                  ⚫️ Количество удаленных (показывает количество удаленных фильмов)
                  ⚫️ Количество добавленных фильмов (показывает количество добавленных фильмов)
                  ⚫️ Удаленные фильмы (показывает список удаленных фильмов)
                  ⚫️ Добавленные фильмы (показывает список добавленных фильмов)
                  ⚫️ Инфо (показывает информацию о пользователе)
                  ⚫️ Добавить любымый фильм (Добавляет фильм в раздел "Любимые")
                  ⚫️ Любимые фильмы (показывает список любимых фильмов)
                  
                  Все эти команды можно написать немного иным способом
                  Так же не забывайте, что написав определенное сообщение, вы можете получить пасхалку!
''')

            print('Чтобы в следующий раз посмотреть список напишите "Список команд"')
            list_f += 1

        elif q_list == 'нет' or q_list == 'Нет':
            list_f += 1

    else:
        random_smile = random.choice(smile_list)
        message = input(f'Чем я могу помочь?{random_smile} ')
        lower_message = message.lower()

        if lower_message == 'привет':
            print('Привет🖐')
            time.sleep(3)

        elif lower_message == 'список команд' or lower_message == 'команды':
            print('''
            Список команд:
                  ⚫️ Команды (показывает список команд)
                  ⚫️ Список фильмов (показывает список фильмов)
                  ⚫️ Добавить фильм (добавляет в список фильм)
                  ⚫️ Удалить фильм (удаляет фильм из списка фильмов)
                  ⚫️ Порекомендуй фильм (бот рекомендует фильм)
                  ⚫️ Количество фильмов (показывает количество фильмов)
                  ⚫️ Добавить просмотренный фильм (добавляет в фильм в "Просмотренное")
                  ⚫️ Список просмотренных (показывает список просмотренных фильмов)
                  ⚫️ Количество просмотренных (показывает число просмотренных фильмов)
                  ⚫️ Количество удаленных (показывает количество удаленных фильмов)
                  ⚫️ Количество добавленных фильмов (показывает количество добавленных фильмов)
                  ⚫️ Удаленные фильмы (показывает список удаленных фильмов)
                  ⚫️ Добавленные фильмы (показывает список добавленных фильмов)
                  ⚫️ Инфо (показывает информацию о пользователе)
                  ⚫️ Добавить любымый фильм (Добавляет фильм в раздел "Любимые")
                  ⚫️ Любимые фильмы (показывает список любимых фильмов)
                  
                  Все эти команды можно написать немного иным способом
                  Так же не забывайте, что написав определенное сообщение, вы можете получить пасхалку!
''')

        elif lower_message == 'покажи список фильмов' or lower_message == 'список фильмов' or lower_message == 'посмотреть спимок фильмов' or lower_message == 'посмотреть список':
            print(f'Список фильмов: {films}')
            time.sleep(3)

        elif lower_message == 'добавь фильм' or lower_message == 'добавить' or lower_message == 'добавить фильм':
            add_film = input('Какой фильм добавить?🤔 ')
            films.append(add_film)
            append_films.append(add_film)
            add_film_counter += 1
            print('Фильм успешно добавлен в список!🙂')
            time.sleep(3)

        elif lower_message == 'удалить фильм' or lower_message == 'удалить фильм из списка' or lower_message == 'удалить':
            print(f'Какой из этих фильмов вы бы хотели удалить?🤔 \n{films}')
            remove_films = input()
            if remove_films in films:
                delete_films_list.append(remove_films)
                films.remove(remove_films)
                delete_film += 1

                print('Вы успешно удалили фильм!')
                time.sleep(3)
            
            else:
                print('Такого фильма в списке нет')
                time.sleep(3)

        elif lower_message == 'порекомендуй фильм' or lower_message == 'рекомендации':
            print(f'Мне очень понравился фильм {films[0]} \nМожете смело смотреть этот фильм!😁')
            time.sleep(3)

        elif lower_message == 'количество фильмов' or lower_message == 'покажи количество фильмов':
            quantity = len(films)
            print('Подсчет количества фильмов...')
            time.sleep(2)
            print(f'Количество фильмов: {quantity}')
            time.sleep(3)

        elif lower_message == 'добавить в список просмотренных фильмов' or lower_message == 'добавить просмотренный фильм' or lower_message == 'добавить фильм в "Просмотренное"' or lower_message == 'добавить фильм в просмотренное' or lower_message == 'добавить в просмотренное':
            view = input('Какой фильм вы посмотрели? ')
            if view in films:
                viewed_films_list.append(view)
                viewed_films += 1
                append_films.append(view)
                time.sleep(3)
                print('Фильм успешно добавлен в список "Просмотренные!"')

            else:
                os.system('cls')
                print('ERROR404')
                time.sleep(1)
                print('Кажется такого фильма нет в списке')
                q_add = input('Добавить? ')
                q_add.lower()
                append_films.append(view)
                if q_add == 'да' or q_add == 'давай':
                    films.append(view)
                    viewed_films_list.append(view)
                    viewed_films += 1
                    for i in range(3):
                        os.system('cls')
                        print('Добавление в список')
                        time.sleep(0.5)

                        os.system('cls')
                        print('Добавление в список.')
                        time.sleep(0.5)

                        os.system('cls')
                        print('Добавление в список..')
                        time.sleep(0.5)

                        os.system('cls')
                        print('Добавление в список...')
                        time.sleep(0.5)

                    print('Фильм автоматически добавлен в список фильмов и список просмотренных фильмов!')
                    time.sleep(3)

                else:
                    print('Возвращяю вас назад')
                    time.sleep(3)

        elif lower_message == 'список просмотренных фильмов' or lower_message == 'список просмотренных':
            print(f'Список просмотренных фильмов: \n{viewed_films_list}')
            time.sleep(3)

        elif lower_message == 'сколько фильмов я посмотрел?' or lower_message == 'сколько фильмов я посмотрела' or lower_message == 'количество просмотренных' or lower_message == 'количество просмотренных фильмов':
            print(f'Вы посмотрели {viewed_films} фильм(ов)!')
            time.sleep(3)

        elif lower_message == 'сколько фильмов я удалил?' or lower_message == 'количество удаленных фильмов' or lower_message == 'сколько фильмов я удалила?' or lower_message == 'количество удаленных':
            print(f'Вы удалили {delete_film} фильм(ов)!')
            time.sleep(3)
        
        elif lower_message == 'сколько фильмов я добавил?' or lower_message == 'сколько фильмов я добавила?' or lower_message == 'количество добавленных фильмов' or lower_message == 'количество добавленных':
            print(f'Вы добавили {add_film_counter} фильм(ов)!')
            time.sleep(3)

        elif lower_message == 'какие фильмы я удалил?' or lower_message == 'какие фильмы я удалила?' or lower_message == 'список удаленных фильмов' or lower_message == 'удаленные фильмы':
            print(f'Вы удалили такие фильмы как: {delete_films_list}')
            time.sleep(3)

        elif lower_message == 'какие фильмы я добавил?' or lower_message == 'какие фильмы я добавила?' or lower_message == 'добавленные фильмы' or lower_message == 'список добавленных фильмов' or lower_message == 'добавленные фильмы':
            print(f'Вы добавили такие фильмы как: {append_films}')
            time.sleep(3)

        elif lower_message == 'инфо' or lower_message == 'моя информация':
            if expansion_of_the_territory == False:
                for i in range(3):
                    os.system('cls')
                    print('Сбор данных')
                    time.sleep(0.5)

                    os.system('cls')
                    print('Сбор данных.')
                    time.sleep(0.5)

                    os.system('cls')
                    print('расширение территории')
                    time.sleep(0.2)

                    os.system('cls')
                    print('Сбор данных..')
                    time.sleep(0.5)

                    os.system('cls')
                    print('Сбор данных...')
                    time.sleep(0.5)
            else:
                for i in range(3):
                    os.system('cls')
                    print('Сбор данных')
                    time.sleep(0.5)

                    os.system('cls')
                    print('Сбор данных.')
                    time.sleep(0.5)

                    os.system('cls')
                    print('Сбор данных..')
                    time.sleep(0.5)

                    os.system('cls')
                    print('Сбор данных...')
                    time.sleep(0.5)

            print()
            print('=' * 35 + f'\nВас зовут: {name} \nВы добавили {add_film_counter} фильмов \nВы удалили {delete_film} фильмов \nВаши любимые фильмы: {favorit_films_list} \nПросмотренно фильмов {viewed_films} \nНайдено пасхалок {achievement_counter}/3 \nЗвания: {achievement} \nМонеты: {money}\n' + 35 * '=')
            time.sleep(3)

        elif lower_message == 'добавить любимый фильм':
            add_favorit = input('Какой фильм добавить в категорию "Любимые"? ')
            if add_favorit in films:
                favorit_films_list.append(add_favorit)
                print("Фильм успешно добавлен в категорию 'Любимые'!")
                time.sleep(3)

            else:
                os.system('cls')
                print('ERROR404')
                time.sleep(1)
                print('Кажется такого фильма нет в списке')
                q_add = input('Добавить?')
                q_add_lower = q_add.lower()
                append_films.append(add_favorit)

                if q_add_lower == 'да' or q_add_lower == 'давай':
                    films.append(view)
                    favorit_films_list.append(add_favorit)
                    for i in range(3):
                        os.system('cls')
                        print('Добавление в список')
                        time.sleep(0.5)

                        os.system('cls')
                        print('Добавление в список.')
                        time.sleep(0.5)

                        os.system('cls')
                        print('Добавление в список..')
                        time.sleep(0.5)

                        os.system('cls')
                        print('Добавление в список...')
                        time.sleep(0.5)
                
                    print('Фильм автоматически добавлен в список любимых фильмов и список просмотренных фильмов!')
                    time.sleep(3)
                
                else:
                    print('Возвращяю вас назад')
                    time.sleep(3)
        elif lower_message == 'список любимых фильмов' or lower_message == 'список любимых' or lower_message == 'любимые фильмы':
            print(f'Любимые фильмы: {favorit_films_list}')

        elif lower_message == 'рандомный фильм' or lower_message == 'покажи рандомный фильм' or lower_message == 'дай рандомный фильм':
            print(f'Итаааак...')
            time.sleep(2)
            random_film = random.choice(films)
            print(f'Вам выпал фильм {random_film}')
            print("Приятного просмотра!")
            time.sleep(3)

        elif lower_message == 'расширение территории':
            if expansion == False:
                expansion = not expansion
                print('\n' + 32 * '=')
                print('Поздравлем, вы нашли пасхалку!')
                achievement_counter += 1
                print('Вы получили звание "Шестиглазый"')
                achievement.append('Шестиглазый')
                time.sleep(1)
                print(f'Найдено пасхалок {achievement_counter}/3')
                print(32 * '=')
                time.sleep(3)

            else:
                print('Вы уже получили пасхалку!')
                time.sleep(2)

        elif lower_message == 'расширение территории' and expansion == True:
            print('Вы уже получили пасхалку!')
            time.sleep(2)

        elif lower_message == 'достань с неба луну':
            if moon == False:
                moon = not moon
                print('\n' + 32 * '=')
                print('Поздравляем, вы нашли пасхалку!')
                time.sleep(1)
                print('Вы получили звание "Фантазер"!')
                achievement_counter += 1
                achievement.append('Фантазер')
                time.sleep(1)
                print(f'Найдено пасхалок {achievement_counter}/3')
                print(32 * '=')
                time.sleep(3)

            else:
                print('Вы уже получили пасхалку!')
                time.sleep(2)

        elif lower_message == 'дай монетку' or lower_message == 'дай монет' or lower_message == 'дай деньги' or lower_message == 'дай денег':
            if money_egg == False:
                money_egg = not money_egg
                achievement_counter += 1
                print('Вы получили монетку!')
                money += 1
                time.sleep(1)
                print('=' * 32 + '\nПоздравляем вы нашли пасхалку!')
                print('Вы получили звание "Мистер Крабс"!')
                achievement.append('Мистер Крабс')
                time.sleep(2)
                print(f'Найдено пасхалок {achievement_counter}/3 \n' + '=' * 32)
                time.sleep(3)

            else:
                print(f'Вы получили монетку!')
                money += 1
                    
        elif lower_message == 'пока' or lower_message == 'спасибо' or lower_message == 'спасибо!' or lower_message == 'отключись' or lower_message == 'завершить работу':
            print('Рад был помочь!🤗')
            break

        else:
            print('Такой команды нет😓')
            time.sleep(1)

        if achievement_counter == 3:
            os.system('cls')
            print(f'Поооздравляем!!! Вы нашли все пасхалки! \nЗа это вы получаете звание "Всевидящий"!')
            achievement.append('Всевидящий')
            achievement_counter += 1