class Unit:

    def __init__(self, field, state, speed):
        self.field = field
        self.state = state
        self.speed = speed

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.state == 'is_flyy':
            return self.speed * 1.2
        elif self.state == 'is_crawnawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
