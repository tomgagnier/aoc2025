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
    with open(file_name) as f:
        joltage_banks = f.read().splitlines()
    print(file_name)
    for i, part in enumerate([part1, part2], start=1):
        print(f'    part{i}', sum((part(bank) for bank in joltage_banks)))


solve("example.txt")
solve("input.txt")
