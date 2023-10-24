from typing import Optional

X_CELL = "x"
O_CELL = "0"


class Game:
    def __init__(self, field=None, size=None):
        if field is None:
            self.field = self.create_field(size)
        else:
            self.field = field

        if not self.is_field_correct():
            ...

        self.step_number: int = self.calculate_step_number()
        self.who_win = None

        self.game_end = self.check_winning_conditions()

    def start_game(self):
        if self.game_end:
            return

        result = None
        while self.has_steps():
            step: tuple[int, int] = self.get_step()
            self.set_step(step, self.step_number % 2 == 0)
            result = self.check_winning_conditions()
            if result:
                break

            self.step_number += 1

        self.game_end = True
        self.who_win = result

    def calculate_current_step(self):
        pass

    def create_field(self, size: int) -> list[list]:
        ...

    def is_field_correct(self) -> bool:
        ...

    def has_steps(self):
        pass

    def get_step(self) -> tuple[int, int]:
        pass

    def calculate_step_number(self) -> int:
        pass

    def set_step(self, step, should_i_place_x):
        pass

    def check_winning_conditions(self) -> Optional[str]:
        pass

