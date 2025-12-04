from typing import Callable


def product_ranges(file_name: str) -> list[range]:
    from pathlib import Path
    with open(Path(__file__).parent / file_name) as f:
        return [range(int(r[0]), int(r[1]) + 1) for r in
                map(lambda s: s.split('-'), f.readline().split(','))]


def total_invalid_ids(file_name: str, repeats: Callable[[int], bool]) -> int:
    total = 0
    for product_range in product_ranges(file_name):
        for i in product_range:
            if repeats(i):
                total += i
    return total


def repeats_twice(candidate: int) -> bool:
    s = str(candidate)
    m = len(s) // 2
    return s[0:m] == s[m:]


def part1(file_name: str) -> int:
    return total_invalid_ids(file_name, repeats_twice)


def repeats_n(candidate: int) -> bool:
    s = str(candidate)
    for n in range(2, len(s) + 1):
        if len(s) % n == 0:
            l = len(s) // n
            parts = [s[i * l: (i + 1) * l] for i in range(n)]
            if all(part == parts[0] for part in parts):
                return True
    return False


def part2(file_name: str) -> int:
    return total_invalid_ids(file_name, repeats_n)


def solve(file_name: str):
    for i, part in enumerate([part1, part2], start=1):
        print(f'part{i}', file_name, part(file_name))


solve("example.txt")
solve("input.txt")
