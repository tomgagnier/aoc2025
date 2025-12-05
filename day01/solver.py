MODULUS = 100
START_POSITION = 50

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
    with open(file_name) as f:
        rotations = [(1 if l[0] == 'R' else -1, int(l[1:-1])) for l in f]
    print(file_name)
    for i, part in enumerate([part1, part2], start=1):
        print(f'    part{i}', part(rotations))

solve('example.txt')
solve('input.txt')