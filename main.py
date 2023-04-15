def visits_filter(geo_logs):
    """ Функция возвращает отфильтрованный список geo_logs,
    содержащий только визиты из России."""
    ru_visits = []
    for place in geo_logs:
        variant = str(list(place.values())) 
        RUSSIA = 'Россия'
        if variant.find(RUSSIA) > 0:
            ru_visits.append(place)
    return ru_visits

def unique_values (ids):
    """ Функция выводит уникальные значения из значений словаря"""
    
    result = []
    for ids_user in ids.values():
        result = result + ids_user

    result_unic = set(result)
    return result_unic

def amount_words_in_values (list_values):
    """Функция процентного распределения количества слов среди текстовых значений в списке"""
    zero_word = 0
    one_word = 0
    two_words = 0
    three_words = 0
    many_words = 0

    for element in list_values:
        words = element.split()
        if len(words) == 0:
            zero_word = zero_word + 1 
        elif len(words) == 1:
            one_word = one_word + 1
        elif len(words) == 2:
            two_words = two_words + 1
        elif len(words) == 3:
            three_words = three_words + 1
        else:
            many_words = many_words + 1

    percent_zero = round(zero_word*100/len(queries), 2)
    percent_one = round(one_word*100/len(queries), 2)
    percent_two = round(two_words*100/len(queries), 2)
    percent_three = round(three_words*100/len(queries), 2)
    percent_many = round(many_words*100/len(queries), 2)

    amount_words = {'0': percent_zero,
                    '1': percent_one,
                    '2': percent_two,
                    '3': percent_three,
                    'many': percent_many}
    
    return amount_words



if __name__ == "__main__":
    
    # Задание 1. Визиты из России
    geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
    ]

    print('Фильтр по визитам из России')
    print(visits_filter(geo_logs))
    
    # Задание 2. Список без повторов
    ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

    print('\nУникальные значения id:')
    print(unique_values(ids))

    # Задание 3. Распределение количества слов
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт',
        'футбол'
    ]
    
    print('\nПроцентное распределения количества слов в строках')
    print(amount_words_in_values(queries))
