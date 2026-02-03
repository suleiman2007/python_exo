def solve_skyscrapers(puzzle):
    size = len(puzzle)
    for i in range(size):
        for j in range(size):
            if puzzle[i][j] == 0:
                possible_values = set(range(1, size+1))
                for k in range(size):
                    possible_values -= set([puzzle[i][k], puzzle[k][j]])
                if len(possible_values) == 1:
                    puzzle[i][j] = possible_values.pop()
                    continue
                for value in possible_values:
                    puzzle[i][j] = value
                    if is_valid(puzzle) and solve_skyscrapers(puzzle):
                        return puzzle
                puzzle[i][j] = 0
                return False
    return puzzle

def is_valid(puzzle):
    size = len(puzzle)
    for i in range(size):
        for j in range(size):
            if puzzle[i][j] == 0:
                continue
            for k in range(size):
                if k != j and puzzle[i][j] == puzzle[i][k]:
                    return False
                if k != i and puzzle[i][j] == puzzle[k][j]:
                    return False
            if not check_visibility(puzzle, i, j):
                return False
    return True

def check_visibility(puzzle, row, col):
    size = len(puzzle)
    highest_row = highest_col = 0
    for i in range(size):
        if puzzle[i][col] > highest_row:
            highest_row += 1
        if puzzle[row][i] > highest_col:
            highest_col += 1
    if puzzle[row][col] != highest_row or puzzle[row][col] != highest_col:
        return False
    return True

