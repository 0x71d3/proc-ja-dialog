import glob
import re

pairs = []

for data in sorted(glob.glob('nucc/data???.txt')):
    with open(data) as f:
        prev_code = prev_text = ''
        code = text = ''

        for line in f:
            if line[0] in ['＠', '％']:
                continue

            if '：' in line:
                text = re.sub(r'（.*?）|＜.*?＞|（＜.*?＞）|【.*?】', '', text)

                if not re.match(r'[FM][0-9]{3}|Ｘ', code):
                    code = ''
                if '＊' in text:
                    text = ''

                if (
                    prev_code and code and prev_text and text
                    and prev_code != code
                ):
                    pairs.append((prev_text, text))

                prev_code, prev_text = code, text
                code, text = line.rstrip().split('：', maxsplit=1)

            else:
                text += line.rstrip()

with open('nucc.tsv', 'w') as f:
    for pair in pairs:
        f.write('\t'.join(pair) + '\n')
