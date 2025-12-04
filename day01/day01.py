MODULUS = 100
START_POSITION = 50


def to_rotations(file_name: str) -> list[tuple[int, int]]:
    from pathlib import Path
    with open(Path(__file__).parent / file_name) as f:
        return [(1 if l[0] == 'R' else -1, int(l[1:-1])) for l in f]


def part1(rotations: list[tuple[int, int]]) -> int:
    password = 0
    position = START_POSITION
    for direction, clicks in rotations:
        position += direction * clicks
        password += 0 if position % MODULUS else 1
    return password


def part2(rotations: list[tuple[int, int]]) -> int:
    password = 0
    position = START_POSITION
    for direction, clicks in rotations:
        last_position = position
        quotient, remainder = divmod(clicks, MODULUS)
        password += quotient
        position += direction * remainder
        if position == 0:
            password += 1
        elif position < 0:
            position += MODULUS
            password += 1 if last_position else 0
        elif position >= MODULUS:
            position -= MODULUS
            password += 1 if last_position else 0
    return password


def solve(file_name: str):
    rotations = to_rotations(file_name)
    for i, part in enumerate([part1, part2], start=1):
        print(file_name, f'part{i}', part(rotations))


solve("example.txt")
solve("input.txt")
