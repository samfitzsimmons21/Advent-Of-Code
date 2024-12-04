def part1_solver(word_search: list[str]) -> int:
    # search is 140x140
    # gameplan: search by letter until we find X, then search in each direction until we find the rest of XMAS
    # return the count of XMAS in the search
    total = 0
    i = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, -1), (-1, 0)]
    while i < len(word_search):
        j = 0
        while j < len(word_search[i]):
            if word_search[i][j] == "X":
                valid_directions = directions.copy()

                # check that we can go in each direction
                for direction in directions:
                    if (
                        i + 3 * direction[0] < 0
                        or i + 3 * direction[0] >= len(word_search)
                        or j + 3 * direction[1] < 0
                        or j + 3 * direction[1] >= len(word_search[i])
                    ):
                        valid_directions.remove(direction)

                for d in valid_directions:
                    if word_search[i + d[0]][j + d[1]] == "M":
                        if word_search[i + 2 * d[0]][j + 2 * d[1]] == "A":
                            if word_search[i + 3 * d[0]][j + 3 * d[1]] == "S":
                                total += 1

            j += 1
        i += 1

    return total


def part2_solver(word_search: list[str]) -> int:
    # Now need to look for 3x3 squares of the form [MAS] diagonally in both diagonals (direction agnostic). Two examples:
    # Important observation: 'A' must be in the center. We can use that as a search key to identify potential squares
    pt2_total = 0
    i = 1
    while i < len(word_search) - 1:
        j = 1
        while j < len(word_search[i]) - 1:
            if word_search[i][j] == "A":
                # get relevant cells
                top_left = word_search[i - 1][j - 1]
                top_right = word_search[i - 1][j + 1]
                bottom_left = word_search[i + 1][j - 1]
                bottom_right = word_search[i + 1][j + 1]

                if (top_left == "S" and bottom_right == "M") or (
                    top_left == "M" and bottom_right == "S"
                ):
                    if (top_right == "S" and bottom_left == "M") or (
                        top_right == "M" and bottom_left == "S"
                    ):
                        pt2_total += 1
            j += 1
        i += 1

    return pt2_total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        word_search = f.read().splitlines()

    print(f"'XMAS' count: {part1_solver(word_search)}")
    print(f"'X-MAS' count: {part2_solver(word_search)}")