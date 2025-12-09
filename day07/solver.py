from collections import Counter

for file_name in 'example.txt', 'input.txt':
    rows = open(file_name).readlines()
    timelines = Counter()
    timelines[rows[0].index('S')] = 1
    beam_splits = 0
    for row in rows[1:]:
        for (i, c) in enumerate(row):
            if c == '^':
                beam_splits += 1
                # Add the positions of the rows above and below the current one
                timelines[i - 1] += timelines[i]
                timelines[i + 1] += timelines[i]
                # Remove the current row from the list of end positions
                del timelines[i]
    print(file_name)
    print('  part1', beam_splits)
    print('  part2', timelines.total())
