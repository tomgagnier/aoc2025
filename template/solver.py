def part1():
    pass

def part2():
    pass

def solve(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
        paragraphs = [text.splitlines() for text in f.read().split('\n\n')]
    print(file_name)
    for i, part in enumerate([part1, part2], start=1):
        print(f'  part{i}', part())

solve("example.txt")
# solve("input.txt")