def merge(ranges: list[range]) -> list[range]:
    result: list[range] = []
    for r in sorted(ranges, key=lambda x: x.start):
        if result and result[-1].stop >= r.start:
            result[-1] = range(result[-1].start, max(result[-1].stop, r.stop))
        else:
            result.append(r)
    return result

def solve(file_name: str):
    with (open(file_name) as f):
        paragraphs = [text.splitlines() for text in f.read().split('\n\n')]

    fresh_ingredient_ranges = merge(
        [range(start, end + 1)
         for start, end in (map(int, r.split('-')) for r in paragraphs[0])]
    )

    ingredients = sorted(map(int, paragraphs[1]))

    print(file_name)
    print('    part1', sum(1 for i in ingredients if any(i in r for r in fresh_ingredient_ranges)))
    print('    part2', sum(r.stop - r.start for r in fresh_ingredient_ranges))


solve("example.txt")
solve("input.txt")