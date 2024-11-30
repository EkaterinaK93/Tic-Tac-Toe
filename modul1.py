def play_game():
    # Инициализация карты
    maps = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]

    # Инициализация победных линий
    victories = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]

    # Вывод карты на экран
    def print_maps():
        print(maps[0], end=" ")
        print(maps[1], end=" ")
        print(maps[2])

        print(maps[3], end=" ")
        print(maps[4], end=" ")
        print(maps[5])

        print(maps[6], end=" ")
        print(maps[7], end=" ")
        print(maps[8])

    # Сделать ход в ячейку
    def step_maps(step, symbol):
        ind = maps.index(step)
        maps[ind] = symbol

    # Получить текущий результат игры
    def get_result():
        win = ""

        for i in victories:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                win = "X"
            if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
                win = "O"

        return win

    # Проверка на ничью
    def check_draw():
        return all(isinstance(cell, str) for cell in maps)

    # Основная программа
    game_over = False
    player1 = True
    invalid_attempts = 0

    while not game_over:

        # 1. Показываем карту
        print_maps()

        # 2. Запрос ввода хода
        while True:
            if player1:
                symbol = "X"
                step = input("Человек 1, ваш ход: ")
            else:
                symbol = "O"
                step = input("Человек 2, ваш ход: ")

            # Проверка на ввод корректных данных
            try:
                step = int(step)
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue

            if step in maps:
                # Проверка, не занята ли клетка
                if maps[maps.index(step)] in ["X", "O"]:
                    print("Указанная вами цифра занята, введите свободную цифру из поля: ")
                    invalid_attempts += 1
                    if invalid_attempts >= 2:  # Завершаем игру при двух ошибках
                        print("Игрок слишком много раз ввел неверные данные. Игра окончена.")
                        return
                else:
                    step_maps(step, symbol)  # убираем цикл если введено корректное значение
                    break
            else:
                print("Указанная вами цифра отсутствует или занята, введите свободную цифру из поля")
                invalid_attempts += 1
                if invalid_attempts >= 2:  # Завершаем игру при двух ошибках
                    print("Игрок слишком много раз ввел неверные данные. Игра окончена.")
                    return

        win = get_result()  # Определим победителя

        if win != "":
            game_over = True
        elif check_draw():  # Проверка на ничью
            game_over = True
        else:
            game_over = False

        player1 = not player1
        invalid_attempts = 0  # Сброс попыток после успешного хода

    # Игра окончена. Покажем карту. Объявим победителя или ничью.
    print_maps()
    if win:
        print("Победил", win)
    else:
        print("Никто не победил")


# Основной цикл для перезапуска игры
def main():
    while True:
        play_game()
        restart = input("Ещё партию? (да/нет): ").strip().lower()
        if restart != "да":
            break


if __name__ == "__main__":
    main()