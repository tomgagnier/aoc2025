from typing import Callable


def total_invalid_ids(product_ranges: list[range],
                      invalid: Callable[[int], bool]) -> int:
    return sum(
        i
        for product_range in product_ranges
        for i in product_range
        if invalid(i)
    )


def part1(product_ranges: list[range]) -> int:
    def repeats_twice(candidate: int) -> bool:
        s = str(candidate)
        m = len(s) // 2
        return s[0:m] == s[m:]

    return total_invalid_ids(product_ranges, repeats_twice)


def part2(product_ranges: list[range]) -> int:
    def repeats_n(candidate: int) -> bool:
        s = str(candidate)
        for n in range(2, len(s) + 1):
            if len(s) % n == 0:
                l = len(s) // n
                parts = [s[i * l: (i + 1) * l] for i in range(n)]
                if all(part == parts[0] for part in parts):
                    return True
        return False

    return total_invalid_ids(product_ranges, repeats_n)


def solve(file_name: str):
    with open(file_name) as f:
        product_ranges = [range(int(r[0]), int(r[1]) + 1) for r in
                          map(lambda s: s.split('-'), f.readline().split(','))]
    print(file_name)
    for i, part in enumerate([part1, part2], start=1):
        print(f'    part{i}', part(product_ranges))


solve("example.txt")
solve("input.txt")
