'''Приветствие'''
print ("-"*65)
print("<"* 13, "Добро пожаловать в Крестики-Нолики!", ">"*13)
print("<"*20, "Игра для двоих", ">"*20)
print("<"*20, "Ход формата x,y.", ">"*20)
print("<"*15, "Х - строка, У - столбик.", ">"*15)
print("<"*20, "Удaчи!", ">"*30)
print("-"*65)


'''Функция создания игрового поля'''
def create_field():
    print(f"  | 0 | 1 | 2 |")
    print ("-"*15)
    for i, row in enumerate(field):
        row_str = f"{i} | {' | '.join(row)} | "
        print(row_str)
        print("-"*15)

"""Функция хода с дополнительными проверками правильности ввода данных"""
def move():
    while True:
        cords = input("Ваш ход:").split()
        '''Если длина вводимых координат больше двух чисел - ошибка'''
        if len(cords) != 2:
            print("Неверные координаты. Введите два числа через пробел!")
            continue

        x,y = cords
        """Если введенные координаты являются не числами - ошибка"""
        if not (x.isdigit()) or not (y.isdigit()):
            print("Неверные координаты. Введенные координаты должны быть числами.")
            continue

        x,y = int(x), int(y)
        """Если введенные координаты не попадают в выбранный игровой диапазон - ошибка"""
        if 0> x or x>2 or 0>y or y>2:
            print("Неверные координаты. Выберите клетку в диапазоне от 0 0 до 2 2!")
            continue
        """Если выбрана занятая клетка - ошибка"""
        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x,y

"""Функция проверки победителя"""
def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols =[]
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X","X","X"]:
            print("Поздравляем! Выиграл X!")
            return True
        if symbols == ["0","0","0"]:
            print("Поздравляем! Выиграл 0!")
            return True
    return False



field = [[" "] * 3 for _ in range(3)]
count = 0
while True:
    count+=1
    create_field()
    if count%2==1:
        print ("Ходит Х")
    else:
        print ("Ходит 0")

    x,y = move()

    if count%2==1:
       field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count==9:
        break
        print("Ничья!")


