# Создаём поле
board = [' ' for _ in range(9)]  # 9 ячеек (3x3)
current_player = 'X'

# Функция отображения поля
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Проверка на победу
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикали
        [0, 4, 8], [2, 4, 6]              # диагонали
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Проверка на ничью
def check_draw():
    return ' ' not in board

# Основная логика игры
def play_game():
    global current_player

    while True:
        print_board()
        try:
            move = int(input(f"Игрок {current_player}, введите номер ячейки (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Неверный ход, ячейка занята или номер вне диапазона.")
                continue
        except ValueError:
            print("Введите число от 1 до 9.")
            continue

        board[move] = current_player

        if check_win(current_player):
            print_board()
            print(f"Игрок {current_player} выиграл!")
            break

        if check_draw():
            print_board()
            print("Ничья!")
            break

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'

# Запуск игры
play_game()
