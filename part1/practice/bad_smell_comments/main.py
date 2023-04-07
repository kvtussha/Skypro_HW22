# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def move(self, field, coordinate_x, coordinate_y, direction, is_fly, is_crawn, speed = 1):

        if is_fly and is_crawn:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = coordinate_y + speed
                new_x = coordinate_x
            elif direction == 'DOWN':
                new_y = coordinate_y - speed
                new_x = coordinate_x
            elif direction == 'LEFT':
                new_y = coordinate_y
                new_x = coordinate_x - speed
            elif direction == 'RIGHT':
                new_y = coordinate_y
                new_x = coordinate_x + speed
        if is_crawn:
            speed *= 0.5
            if direction == 'UP':
                new_y = coordinate_y + speed
                new_x = coordinate_x
            elif direction == 'DOWN':
                new_y = coordinate_y - speed
                new_x = coordinate_x
            elif direction == 'LEFT':
                new_y = coordinate_y
                new_x = coordinate_x - speed
            elif direction == 'RIGHT':
                new_y = coordinate_y
                new_x = coordinate_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

