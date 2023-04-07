class Unit:
    def move(self, field, x_coord: int, y_coord: int, direction, is_is_flyy: bool, is_crawnawl: bool, speed: int = 1):

        if is_is_flyy and is_crawnawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_is_flyy:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed
        if is_crawnawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

