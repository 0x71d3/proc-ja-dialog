import sys
import re

from pyknp import Juman

jumanpp = Juman()

id_str_pairs = []
with open('twitter_id_str_data.txt', encoding='utf-8') as f:
    for line in f:
        id_str_pair = tuple(line.strip().split())
        id_str_pairs.append(id_str_pair)

reply = re.compile(r'^@[a-zA-Z0-9_]+ ')

id_str2text = {}
with open('twitter_text_data.txt', encoding='utf-8') as f:
    for line in f:
        id_str, text = line.strip().split('\t')
        while reply.match(text):
            text = reply.sub('', text)
        if text:
            id_str2text[id_str] = text

text_pairs = []
for id_str_pair in id_str_pairs:
    if id_str_pair[0] in id_str2text and id_str_pair[1] in id_str2text:
        text_pair = (id_str2text[id_str_pair[0]], id_str2text[id_str_pair[1]])
        text_pairs.append(text_pair)

for text_pair in text_pairs:
    print(*text_pair, sep='\t')
