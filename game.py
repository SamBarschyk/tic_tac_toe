from typing import Optional
X_CELL = "X"
O_CELL = "O"
class Game:
    def __init__(self, field=None, size=None):
        if field is None:
            self.field = self.create_field(size)
        else:
            self.field = field
        if not self.is_field_correct():
            print("Поле не коректне")
        self.step_number: int = self.calculate_step_number()
        self.who_win = None
        self.game_end = self.check_winning_conditions()

    def start_game(self):
        if self.game_end:
            return
        print("Гра почалася. Ласкаво просимо!")
        result = None
        while self.has_steps():
            self.print_board()
            step: tuple[int, int] = self.get_step()
            self.set_step(step, self.step_number % 2 == 0)
            result = self.check_winning_conditions()
            if result:
                break
            self.step_number += 1
        self.print_board()
        self.game_end = True
        self.who_win = result

    def calculate_current_step(self):
        return X_CELL if self.step_number % 2 == 0 else O_CELL
    def create_field(self, size: int) -> list[list]:
        field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        return field
    def is_field_correct(self) -> bool:
        for row in self.field:
            for cell in row:
                if cell not in [X_CELL, O_CELL, ' ']:
                    print("Некоректне значення в клітинці:", cell)
                    return False
        print("Всі клітинки мають коректні значення.")
        return True

    def has_steps(self):
        for row in self.field:
            for cell in row:
                if cell == ' ':
                    return True
        return False

    def get_step(self) -> tuple[int, int]:
        while True:
            user_input = input("Введіть номер рядка та стовпця через пробіл (наприклад, '1 1'): ")
            input_values = user_input.split()

            if len(input_values) != 2:
                print("Введіть два числа через пробіл. Спробуйте ще раз.")
                continue

            try:
                row, col = map(int, input_values)
                if 1 <= row <= len(self.field) and 1 <= col <= len(self.field[0]) and self.field[row - 1][
                    col - 1] == ' ':
                    return row - 1, col - 1  # Зменшуємо на 1, оскільки індексація починається з 0
                print("Невірні координати або клітинка вже зайнята. Спробуйте ще раз.")
            except ValueError:
                print("Введіть числові значення заново.")

    def calculate_step_number(self) -> int:
        return sum(1 for row in self.field for cell in row if cell != ' ')
    def set_step(self, step, should_i_place_x):
        row, col = step
        player_symbol = X_CELL if should_i_place_x else O_CELL
        self.field[row][col] = player_symbol
    def check_winning_conditions(self) -> Optional[str]:
        for row in range(3):
            if self.field[row][0] == self.field[row][1] == self.field[row][2] and self.field[row][0] != ' ':
                return self.field[row][0]
            if self.field[0][row] == self.field[1][row] == self.field[2][row] and self.field[0][row] != ' ':
                return self.field[0][row]
        if self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != ' ':
            return self.field[0][0]
        if self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[0][2] != ' ':
            return self.field[0][2]
        return None
    def print_board(self):
        for row in self.field:
            print(" | ".join(row))
            print("-" * 9)
if __name__ == '__main__':
    game = Game()
    game.start_game()
    if game.who_win is None:
        print('Нічия')
    elif game.who_win == X_CELL:
        print(f"Виграв {X_CELL}")
    elif game.who_win == O_CELL:
        print(f"Виграв {O_CELL}")

