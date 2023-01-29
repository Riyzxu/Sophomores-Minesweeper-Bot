import random


def get_mine_neighbors(x, y, rows, cols, board):
    mines = []
    neighbors = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1),
                 (x - 1, y - 1)]
    for n in neighbors:
        if 0 <= n[0] <= cols - 1 and 0 <= n[1] <= rows - 1:
            if board[n[0]][n[1]] == 9:
                mines.append(n)
    return mines


def generate_board(row, col, mines, show=False, look=True, reveal=False):
    rows = row
    cols = col
    num_mines = mines
    show_mines = show
    better_look = look
    reveal_board = reveal

    board = [[0 for i in range(0, rows)] for j in range(0, cols)]

    board_coordinates = [(x, y) for x in range(0, cols) for y in range(0, rows)]
    mine_coordinates = random.sample(board_coordinates, num_mines)

    for mine in mine_coordinates:
        x, y = mine
        board[x][y] = 9
        neighbors = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1),
                     (x - 1, y - 1)]
        for n in neighbors:
            if 0 <= n[0] <= cols - 1 and 0 <= n[1] <= rows - 1 and n not in mine_coordinates:
                board[n[0]][n[1]] += 1

    for i in range(0, cols):
        for j in range(0, rows):
            sq = board[i][j]
            if 0 < sq < 9:
                mine_neighbors = get_mine_neighbors(i, j, rows, cols, board)
                if sq != len(mine_neighbors):
                    print("not consistent!")

    board_formatted = ""

    emojis = "🟦 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 💥".split()

    for i in range(0, cols):
        for j in range(0, rows):
            num = board[i][j]
            if better_look:
                if reveal_board:
                    board_formatted += f"{emojis[num]}"
                else:
                    board_formatted += f"||{emojis[num]}||"
            else:

                if num == 9:
                    num = "B"
                if num == 1:
                    num = "1 "

                board_formatted += f"|| {num} ||  "

                if show_mines:
                    print(f"|| {num} ||", end="  ")

        board_formatted += "\n"
        if show_mines:
            print()

    return board_formatted


if __name__ == "__main__":
    print(generate_board(10, 10, 95, True, True, True))
