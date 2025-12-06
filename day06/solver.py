import itertools
from functools import reduce


def rotate(matrix: list[list[str]]) -> list[list[str]]:
    return [list(row[::-1]) for row in zip(*matrix[::-1])]

def evaluate(operation: list[str]) -> int:
    *operands, operator = operation
    if operator == '*':
        return reduce(lambda x, y: x * int(y), map(int, operands), 1)
    else:
        return sum(map(int, operands))


def part1(lines: list[str]) -> int:
    operations = rotate([line.split() for line in lines])
    return sum(map(evaluate, operations))


def part2(lines: list[str]) -> int:
    max_line_length = max(len(v) for v in lines)
    padded_operand_lines = [
        v.ljust(max_line_length)
        for v in (lines[:-1])
    ]
    rotated_operands = [
        ''.join(row).strip()
        for row in (rotate([list(v) for v in padded_operand_lines]))
    ]
    operands = [
        list(group)
        for key, group
        in itertools.groupby(rotated_operands, key=lambda x: x == '')
        if not key
    ]
    operations = [
        operand + [operator]
        for operand, operator
        in zip(operands, lines[-1].split())
    ]
    return sum(map(evaluate, operations))


def solve(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    print(file_name)
    for i, part in enumerate([part1, part2], start=1):
        print(f'  part{i}', part(lines))


solve("example.txt")
solve("input.txt")
