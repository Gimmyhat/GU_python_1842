import os

root_dir = os.getcwd()
stat_dict = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0,
    1000000: 0
}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        size_file = os.path.getsize(os.path.join(root, file))
        if size_file <= 100:
            stat_dict[100] += 1
        elif 100< size_file <= 1000:
            stat_dict[1000] += 1
        elif 1000< size_file <= 10000:
            stat_dict[10000] += 1
        elif 10000< size_file <= 100000:
            stat_dict[100000] += 1
        elif 100000< size_file <= 1000000:
            stat_dict[1000000] += 1
print(stat_dict)

