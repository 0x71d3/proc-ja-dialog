import glob
from collections import Counter

counter = Counter()

for data in sorted(glob.glob('nucc/data???.txt')):
    with open(data) as f:
        for line in f:
            if line[0] in ['＠', '％']:
                continue

            if '：' in line:
                code, _ = line.rstrip().split('：', maxsplit=1)
                counter[code] += 1

print(counter)
