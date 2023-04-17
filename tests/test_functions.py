import pytest
from main import visits_filter, unique_values, amount_words_in_values 

# Тесты для функции visits_filter

def test_Russia_len_list_of_values():
    geo_logs = [
        {'visit1': ['Париж', 'Франция']},
        {'visit2': ['Лиссабон', 'Португалия']},
        {'visit3': ['Дели', 'Индия']},
        {'visit4': ['Архангельск', 'Россия']}
        ]
    
    rez = visits_filter(geo_logs)
    assert isinstance (rez, list)
    assert len(rez) != 0
    assert len(rez) == 1
    

def test_Russia_is_in_values():
    geo_logs = [
        {'visit1': ['Париж', 'Франция']},
        {'visit2': ['Лиссабон', 'Португалия']},
        {'visit3': ['Курск', 'Россия']},
        {'visit4': ['Архангельск', 'Россия']}
        ]
    
    rez = visits_filter(geo_logs)
    assert {'visit3': ['Курск', 'Россия']} in rez
    assert {'visit2': ['Лиссабон', 'Португалия']} not in rez


@pytest.mark.parametrize('geo_logs, expected',
    [([
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']}
    ], [
    {'visit1': ['Москва', 'Россия']},
    {'visit3': ['Владимир', 'Россия']}
    ]),
    ([
    {'visit1': ['Лиссабон', 'Португалия']},
    {'visit2': ['Тула', 'Россия']},
    {'visit3': ['Тула', 'Россия']},
    {'visit4': ['Курск', 'Россия']},
    {'visit5': ['Архангельск', 'Россия']}   
    ], [
    {'visit2': ['Тула', 'Россия']},
    {'visit3': ['Тула', 'Россия']},
    {'visit4': ['Курск', 'Россия']},
    {'visit5': ['Архангельск', 'Россия']}   
    ])]
    )   
def test_Russia_list_of_values(geo_logs, expected):
    rez = visits_filter(geo_logs)
    assert rez == expected


# Тесты для функции unique_values

def test_uniq_values():
    ids = {'user1': [34, 23, 34, 22],
           'user2': [12, 111, 657, 12],
           'user3': [3, 78, 3, 54]}

    rez = unique_values(ids)
    assert isinstance (rez, set)
    assert len(rez) == 9

@pytest.mark.parametrize('ids, expected',
    [({'user1': [3, 54, 5, 34],
       'user2': [10, 123, 123, 12],
       'user3': [36, 15, 9, 15]},
    {3, 54, 5, 34, 10, 123, 12, 36, 15, 9})]
    )
def test_unique_list_of_values(ids, expected):
    rez = unique_values(ids)
    assert rez == expected

# Тесты для функции amount_words_in_values

def test_amount_words_dict_keys_and_values():
    list_values = ['передачи о животных', 
                   'афиша',
                   'курс обучения',
                   '']
    
    
    rez = amount_words_in_values(list_values)
    
    #assert rez == {'0': 25.0, '1': 25.0, '2': 25.0, '3': 25.0, 'many': 0.0}
    assert isinstance(rez, dict)
    assert 25.0 in rez.values()
    assert ['0', '1', '2', '3', 'many'] == list(rez.keys())

@pytest.mark.parametrize('list_values, expected',
    [([
        'сериалы онлайн',
        'новости спорта',
        'афиша',
        'курс доллара',
        'сериалы и детективные истории',
        'сводки новостей',
        'про спорт',
        'футбольные трансляции'
    ],
    {'0': 0.0, '1': 12.5, '2': 75.0, '3': 0.0, 'many': 12.5}),
    ([
        'сериалы',
        'новости',
        '',
        'юмористические передачи',
        'сериалы для большой компании',
        'курс докментальных передч',
        'спорт',
        'экономические сводки'
    ],
    {'0': 12.5, '1': 37.5, '2': 25.0, '3': 12.5, 'many': 12.5})]

    )
def test_amount_words_in_values(list_values, expected):
    rez = amount_words_in_values(list_values)
    assert rez == expected