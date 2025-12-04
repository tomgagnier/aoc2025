def voltage_banks(file_name: str) -> list[str]:
    from pathlib import Path
    with open(Path(__file__).parent / file_name) as f:
        return [line.rstrip('\n') for line in f]


def part1(bank: str) -> int:
    first_digit_pos = bank.index(max(bank[0:-1]))
    max_after_first = max(bank[first_digit_pos + 1:])
    return 10 * int(bank[first_digit_pos]) + int(max_after_first)


def part2(bank: str) -> int:
    voltage = ''
    start = 0
    for n in range(12, 0, -1):
        sub = bank[start:len(bank) - n + 1]
        digit = max(sub)
        pos = start + sub.index(digit)
        voltage += bank[pos]
        start = pos + 1

    return int(voltage)


def solve(file_name: str):
    banks = voltage_banks(file_name)
    for i, part in enumerate([part1, part2], start=1):
        print(f'part{i}', file_name, sum((part(bank) for bank in banks)))


solve("example.txt")
solve("input.txt")
