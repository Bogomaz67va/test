from collections import Counter
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    result = list()
    for item in contacts_list:
        lastname = re.split(" ", item[0])
        firstname = re.split(" ", item[1])
        surname = re.split(" ", item[2])
        initials = lastname + firstname + surname
        new_elem = []
        new_elem.append(initials[0])
        new_elem.append(initials[1])
        new_elem.append(initials[2])
        new_elem.append(item[3])
        new_elem.append(item[4])
        new_elem.append(item[5])
        new_elem.append(item[6])
        result.append(new_elem)
    print(result)
        # result_list = list()
        # result_list.append(item[:3])
        # result_list.append(item[4])
        # result_list.append(item[5])
        # result_list.append(item[6])
        # result.append(result_list)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
