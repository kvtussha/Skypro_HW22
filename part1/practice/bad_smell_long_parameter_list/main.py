# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, state, speed, field):
        self.field = field
        self.state = state
        self.speed = speed

    def _get_speed(self):
        if self.state == 'is_flyy':
            self.speed *= 1.2
        elif self.state == 'is_crawnawl':
            self.speed *= 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')


    def direction(self, x_coord, y_coord, direction,):
        speed = self._get_speed()
        if direction == 'UP':
            self.field.set_unit(x=x_coord, y=y_coord + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=x_coord, y=y_coord - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=x_coord - speed, y=y_coord, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=x_coord + speed, y=y_coord, unit=self)

