# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)
def _read(data: list):
    return [line.split(';') for line in csv.split('\n')]

def _filter(_new_data):
    return [person for person in _new_data if person[1] < 10]

def _sort(data: dict):
    sorted(data, key= lambda person: person[1])


if __name__ == '__main__':
    print(get_users_list())
