class Game:
    def __init__(self):
        self.board = ["*", "*", "*",
                      "*", "*", "*",
                      "*", "*", "*"]
        self.player = None
        self.victory = False

    @staticmethod
    def main_menu():
        print("KÓŁKO I KRZYŻYK\n"
              "1 - Gra z komputerem\n"
              "2 - Gra z innym graczem\n")
        while True:
            decision = input("> ")
            if decision == "1" or decision == "2":
                if decision == "2":
                    session = Game()
                    session.main_loop(1)
                    break
            else:
                print("Nieprawidłowa wartość!")

    def main_loop(self, mode: int):
        if mode == 1:
            self.render()
            while True:
                self.player = "X"
                self.player_turn()
                self.player = "O"
                self.player_turn()

    def render(self):
        board = ""
        for i, field in enumerate(self.board):
            i += 1
            if i % 3 != 0:
                board = board + " " + field
            else:
                board = board + " " + field + "\n"
            i += 1
        print(board)

    def player_turn(self):
        while True:
            if self.player == "X":
                field = int(input("Gracz 1 (Krzyżyk)\n"
                                  "> "))
            else:
                field = int(input("Gracz 2 (Kółko)\n"
                                  "> "))
            if field < 0 or field > 8:
                print("Nieprawidłowa wartość! Prawidłowe wartości pól mieszczą się w przedziale od 0 do 8\n")
                self.render()
            else:
                if self.check_field(field):
                    self.change_field(field, self.player)
                    if self.is_victory() is True and self.player == "X":
                        print("Wygrał Gracz 1")
                        self.victory = True
                        self.main_menu()
                    elif self.is_victory() is True and self.player == "O":
                        print("Wygrał Gracz 2")
                        self.victory = True
                        self.main_menu()
                    elif self.is_victory() == "draw":
                        print("Remis")
                        self.main_menu()
                    break
                else:
                    print("To pole jest już zajęte!")
                    self.render()

    def check_field(self, field: int):
        if self.board[field] == "*":
            return True
        else:
            return False

    def is_victory(self):
        victory_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        if self.board.count("*") == 0:
            return "draw"
        else:
            for combination in victory_combinations:
                fields = ""
                for field in combination:
                    field = self.board[field]
                    if field != "*":
                        fields = fields + field
                    if fields.count("X") == 3 or fields.count("O") == 3:
                        return True
            return False

    def change_field(self, field: int, char: str):
        self.board[field] = char
        self.render()

if __name__ == "__main__":
    game = Game()
    game.main_menu()
