from typing import Iterator


def neighbors(matrix: list[list[str]], row: int, col: int) -> Iterator[tuple[int, int]]:
    for offset in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        r = row + offset[0]
        c = col + offset[1]
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            yield r, c


def removable_paper_rolls(matrix: list[list[str]]) -> list[tuple[int, int]]:
    return [
        (r, c)
        for r in range(len(matrix))
        for c in range(len(matrix[0]))
        if matrix[r][c] == '@' and
           sum(1 for nr, nc in neighbors(matrix, r, c) if matrix[nr][nc] == '@') < 4
    ]


def part1(matrix: list[list[str]]) -> int:
    return len(removable_paper_rolls(matrix))


def part2(matrix: list[list[str]]) -> int:
    total = 0
    while removable := removable_paper_rolls(matrix):
        total += len(removable)
        for r, c in removable:
            matrix[r][c] = '.'
    return total


for file_name in ['example.txt', 'input.txt']:
    print(file_name)
    from pathlib import Path
    with open(Path(__file__).parent / file_name) as f:
        diagram = [list(line.strip()) for line in f]

    for i, part in enumerate([part1, part2], start=1):
        print(f'    part{i}', part(diagram))
