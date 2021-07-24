import bz2

flat_data = []
with bz2.open('twitter_id_str_data.txt.bz2') as f:
    for line in f:
        flat_data += line.decode().strip().split('\t')

for id_str in flat_data:
    print(id_str)
