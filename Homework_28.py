range_value = int(input('Введите числовое значение от одного до пяти: '))


class ValuelError(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info


def check_value(a, b):
    if range_value < a:
        raise ValuelError(f'Значение должно быть не меньше {a}', [1, 2, 3, 4, 5])
    if range_value > b:
        raise ValuelError(f'Значение должно быть не больше {b}', [1, 2, 3, 4, 5])


try:
    check_value(1, 5)
except ValuelError as e:
    print(e.message)
    print(f'Введите одно значение из списка: {e.info}')
else:
    print('Числовое значение введено верно!')
finally:
    print('Так держать!')
