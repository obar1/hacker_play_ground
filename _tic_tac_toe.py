# write your code here


def ddd_print(*args, **kwargs):
    DDD = False
    # DDD = True
    if DDD:
        print(*args, **kwargs)


class Board:
    XY = ["X", "O"]
    SPACE = "_"

    def __init__(self, board_initial_str):
        self.x = 3
        self.y = 3
        self.board_initial_str = board_initial_str
        self.board_chess = dict()
        # for i in range(self.x):
        #     for j in range(self.y):
        #         self.board_chess[(i, j)] = random.choice(self.XY)

    def from_str(self, str=None):
        if str is None:
            str = self.board_initial_str
        assert len(str) == 9
        for i in range(self.x):
            for j in range(self.y):
                self.board_chess[(i, j)] = str[0]
                str = str[1:]

    def print(self):
        @staticmethod
        def handle_undesrcore_as_space(c):
            return " " if c == Board.SPACE else c

        line = "-" * self.x * 3
        print(line, end="")
        for i in range(self.x):
            print()
            print("|", end=" ")
            for j in range(self.y):
                print(handle_undesrcore_as_space(self.board_chess[(i, j)]), end=" ")
            print("|", end=" ")
        print("\n" + line)

    def analyze(self):
        if (self.does_it_win("X") & self.does_it_win("O")) | self.is_game_impsossible():
            return "Impossible"
        if self.does_it_win("X"):
            return "X wins"
        if self.does_it_win("O"):
            return "O wins"
        if self.is_game_not_finished():
            return "Game not finished"
        if self.is_game_draw():
            return "Draw"
        return "Impossible"

    def does_it_win(self, x_or_y):
        ddd_print(f"DDD Looking for {x_or_y * self.x}")
        # rows
        for i in range(0, self.x):
            row = [self.board_chess[(i, j)] for j in range(0, self.y)]
            ddd_print(f'DDD row {" ".join(row)}')
            if "".join(row) == x_or_y * self.x:
                ddd_print(f"{x_or_y} row {i}")
                return True

        # cols
        for i in range(0, self.x):
            col = [self.board_chess[(j, i)] for j in range(0, self.y)]
            ddd_print(f'DDD col {" ".join(col)}')
            if "".join(col) == x_or_y * self.x:
                ddd_print(f"{x_or_y} col {i}")
                return True

        # diag\
        diag = []
        for i in range(0, self.x):
            j = i
            # ddd_print(f"{i} {j}")
            diag.append(self.board_chess[(i, j)])
        ddd_print(f'DDD diag\\ {" ".join(diag)}')
        if "".join(diag) == x_or_y * self.x:
            ddd_print(f"{x_or_y} diag \\")
            return True

        # diag/
        diag = []
        for i in range(0, self.x):
            j = self.x - i - 1
            # ddd_print(f"{i} {j}")
            diag.append(self.board_chess[(i, j)])
        ddd_print(f'DDD diag/ {" ".join(diag)}')
        if "".join(diag) == x_or_y * self.x:
            ddd_print(f"{x_or_y} diag /")
            return True
        return False

    def is_game_not_finished(self):
        count_x = 0
        count_o = 0
        count_sp = 0
        for i in range(self.x):
            for j in range(self.y):
                if self.board_chess[(i, j)] in ("_", " "):
                    count_sp += 1
                if self.board_chess[(i, j)] in ("X"):
                    count_x += 1
                if self.board_chess[(i, j)] in ("O"):
                    count_o += 1
        if count_sp > 1 & (count_o == 3 | count_x == 3):
            return True
        return False

    def is_game_draw(self):
        count_x = 0
        count_o = 0
        count_sp = 0
        for i in range(self.x):
            for j in range(self.y):
                if self.board_chess[(i, j)] in ("_", " "):
                    count_sp += 1
                if self.board_chess[(i, j)] in ("X"):
                    count_x += 1
                if self.board_chess[(i, j)] in ("O"):
                    count_o += 1
        if count_sp == 0:
            return True
        return False

    def is_game_impsossible(self):
        count_x = 0
        count_o = 0
        count_sp = 0
        for i in range(self.x):
            for j in range(self.y):
                if self.board_chess[(i, j)] in ("_", " "):
                    count_sp += 1
                if self.board_chess[(i, j)] in ("X"):
                    count_x += 1
                if self.board_chess[(i, j)] in ("O"):
                    count_o += 1
        if abs(count_x - count_o) >= 2:
            return True
        return False


class Game:
    def __init__(self, x_or_o, board_initial_str) -> None:
        self.x_or_o = x_or_o
        self.board = Board(board_initial_str)

    def set_x_or_o(self, x_or_o=None):
        if x_or_o is None:
            if self.x_or_o == "X":
                self.x_or_o = "O"
            else:
                self.x_or_o = "X"
        else:
            self.x_or_o = x_or_o
        ddd_print(f"curr x_or_o {self.x_or_o}")

    def from_x_y_to_str_is_empty(self, x: int, y: int):
        proj_xy_in_pos = (x - 1) * self.board.x + (
            y - 1
        )  # project the x,y input on the list
        board_initial_lst = list(self.board.board_initial_str)
        ddd_print(board_initial_lst[proj_xy_in_pos])
        return board_initial_lst[proj_xy_in_pos] == Board.SPACE

    def from_x_y_to_str(self, x: int, y: int):
        ddd_print(self.board.board_initial_str)
        proj_xy_in_pos = (x - 1) * self.board.x + (
            y - 1
        )  # project the x,y input on the list
        board_initial_lst = list(self.board.board_initial_str)
        board_initial_lst[proj_xy_in_pos] = self.x_or_o
        res = "".join(board_initial_lst)
        ddd_print(res)
        return res

    def make_turn(self):
        def ask_input():
            """_summary_
            Analyze user input. If the input is incorrect, inform the user why their input is wrong:
            Print This cell is occupied! Choose another one! if the cell is not empty.
            Print You should enter numbers! if the user enters non-numeric symbols in the coordinates input.
            Print Coordinates should be from 1 to 3! if the user enters coordinates outside the game grid.
            Keep prompting the user to enter the coordinates until the user input is valid.
                        Returns:
                            _type_: _description_
            """
            while True:
                res_x, res_y = None, None
                inp = input()
                ddd_print(inp)
                try:
                    res_x, res_y = int(inp.split(" ")[0]), int(inp.split(" ")[1])
                    if any([res not in [1, 2, 3] for res in (res_x, res_y)]):
                        raise IndexError
                    # Print This cell is occupied! Choose another one! if the cell is not empty.
                    if not self.from_x_y_to_str_is_empty(res_x, res_y):
                        raise LookupError
                except TypeError:
                    print("You should enter numbers!")
                except ValueError:
                    print("You should enter numbers!")
                except IndexError:
                    print("Coordinates should be from 1 to 3!")
                except LookupError:
                    print("This cell is occupied! Choose another one!")
                else:
                    return (res_x, res_y)

        self.board.from_str()
        self.board.print()
        (res_x, res_y) = ask_input()
        self.board.board_initial_str = self.from_x_y_to_str(res_x, res_y)
        self.board.from_str()
        self.board.print()


if __name__ == "__main__":
    # initial_inp = input()
    initial_inp = "_________"
    g = Game("X", initial_inp)
    while True:
        g.make_turn()
        g.set_x_or_o()
        curr_game_status = g.board.analyze()
        ddd_print(curr_game_status)
        if curr_game_status.endswith("wins") or curr_game_status == "Draw":
            print(curr_game_status)
            break
