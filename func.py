import json
import datetime
import requests


def open_json_file():
    """
    Функция читает данные в формте JSON
    :return: возвращает файл в формате JSON
    """
    response = requests.get('https://www.jsonkeeper.com/b/56RP')
    dict = json.loads(response.text)
    return dict


def sort_dict(dict):
    """
    Функция  сортирует список словарей по date
    :return: отсортированный список словарей
    """
    sorted_dict = sorted(dict, key=lambda x: ['date'], reverse=True)
    return sorted_dict


def get_executed(dict_list):
    """
    Функция вывода операций только EXECUTED
    :return: отфильтрованный список словарей
    """
    for dic in dict_list:
        if (not 'state' in dic) or dic['state'].upper() != 'EXECUTED':
            dict_list.remove(dic)
    return dict_list


def replacing_digit(text):
    """
    Функция заменяет цифры в номере счета и карты на *.
    - Номер карты замаскирован и не отображаться целиком, в формате  XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом)
    - Номер счета замаскирован и не отображаться целиком, в формате  **XXXX
    (видны только последние 4 цифры номера счета)
    :return: замаскированные цифры
    """
    if (len(text)) < 20:
        return text
    elif text[0:4] == "Счет":
        return text[0:5] + "**" + text[-4:]
    else:
        return text[0:len(text) - 12] + " " + text[len(text) - 12:len(text) - 10] + "** **** " + text[-4:]


def result_dict(dict_list):
    """
    Функция формирует текст для вывода заданного числа словарей из списка dict_list
    :return: результат текста
    """
    result_text = ""
    if 5 <= len(dict_list):
        for item in range(0, 5):
            dic = dict_list[item]
            result_text += datetime.date.fromisoformat(dic["date"][0:10]).strftime('%d-%m-%Y') + " "
            result_text += dic['description'] + '\n'
            if 'from' in dic:
                result_text += replacing_digit(dic['from'])
            if 'to' in dic:
                result_text += " -> " + replacing_digit(dic['to'])
            result_text += "\n"
            result_text += dic['operationAmount']['amount'] + " "
            result_text += dic['operationAmount']['currency']['name']
            result_text += "\n\n"
    return result_text
