class Board:
    def __init__(self):
        # Создаем пустую игровую доску 3x3
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        # Отображаем игровую доску
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col, player):
        # Проверяем, можно ли сделать ход в указанную клетку и делаем ход
        if self.board[row - 1][col - 1] == " ":
            self.board[row - 1][col - 1] = player
            return True
        else:
            print("Эта клетка уже занята. Попробуйте еще раз.")
            return False

    def check_winner(self, player):
        # Проверяем, есть ли победитель
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def check_draw(self):
        # Проверяем, является ли игра ничьей
        return all(cell != " " for row in self.board for cell in row)


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def switch_player(self):
        # Переключаем текущего игрока
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        while True:
            self.board.display()
            print(f"Ход игрока {self.current_player}")
            row = int(input("Введите номер строки (1, 2, 3): "))
            col = int(input("Введите номер столбца (1, 2, 3): "))

            if 1 <= row <= 3 and 1 <= col <= 3:
                if self.board.make_move(row, col, self.current_player):
                    if self.board.check_winner(self.current_player):
                        self.board.display()
                        print(f"Игрок {self.current_player} победил!")
                        break
                    elif self.board.check_draw():
                        self.board.display()
                        print("Ничья!")
                        break
                    else:
                        self.switch_player()
                else:
                    continue
            else:
                print("Неверные координаты. Попробуйте еще раз.")


if __name__ == "__main__":
    game = Game()
    game.play()
