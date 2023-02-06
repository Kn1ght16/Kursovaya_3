from utils.func import get_executed, replacing_digit, result_dict


def test_replacing_digit():
    assert replacing_digit("Visa Platinum") == "Visa Platinum"
    assert replacing_digit("Счет 59986621134048778289") == "Счет **8289"
    assert replacing_digit("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"
    assert replacing_digit("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert replacing_digit("") == ""


def test_get_executed():
    assert get_executed([{'id': 27192367, 'state': 'EXECUTED', 'date': '2018-12-24T20:16:18.819037',
                          'operationAmount': {'amount': '991.49', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                          'description': 'Перевод со счета на счет', 'from': 'Счет 71687416928274675290',
                          'to': 'Счет 87448526688763159781'}]) == [{'date': '2018-12-24T20:16:18.819037',
                                                                    'description': 'Перевод со счета на счет',
                                                                    'from': 'Счет 71687416928274675290',
                                                                    'id': 27192367,
                                                                    'operationAmount': {'amount': '991.49',
                                                                                        'currency': {'code': 'RUB',
                                                                                                     'name': 'руб.'}},
                                                                    'state': 'EXECUTED',
                                                                    'to': 'Счет 87448526688763159781'}]
    assert get_executed([{'id': 27192367, 'state': 'CANCELED', 'date': '2018-12-24T20:16:18.819037',
                          'operationAmount': {'amount': '991.49', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                          'description': 'Перевод со счета на счет', 'from': 'Счет 71687416928274675290',
                          'to': 'Счет 87448526688763159781'}]) == []
    assert get_executed([{'id': 27192367, 'state': '', 'date': '2018-12-24T20:16:18.819037',
                          'operationAmount': {'amount': '991.49', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                          'description': 'Перевод со счета на счет', 'from': 'Счет 71687416928274675290',
                          'to': 'Счет 87448526688763159781'}]) == []


def test_result_dict():
    assert result_dict([
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]) == ('26-08-2019 Перевод организации\n'
                'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                '31957.58 руб.\n'
                '\n'
                '03-07-2019 Перевод организации\n'
                'MasterCard 7158 30** **** 6758 -> Счет **5560\n'
                '8221.37 USD\n'
                '\n'
                '30-06-2018 Перевод организации\n'
                'Счет **6952 -> Счет **6702\n'
                '9824.07 USD\n'
                '\n'
                '23-03-2018 Открытие вклада\n'
                ' -> Счет **2431\n'
                '48223.05 руб.\n'
                '\n'
                '04-04-2019 Перевод со счета на счет\n'
                'Счет **8542 -> Счет **4188\n'
                '79114.93 USD\n'
                '\n')
    assert result_dict([]) == ""
