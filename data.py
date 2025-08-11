import os
import csv
ans_part = []


def find_file(folder_tree):
    global ans_part
    if os.path.isdir(folder_tree):
        items = os.listdir(folder_tree)
        for item in items:
            item_path = os.path.join(folder_tree, item)
            find_file(item_path)
    if '.csv' in folder_tree:
        file = open(folder_tree)
        next(file)
        read = csv.reader(file, delimiter=',')
        for x in read:
            ans_part.append(x)
        ans_part = sorted(ans_part, key=lambda x: (-int(x[-1]), x[-3], x[-2]))


find_file('data')
with open('rating.csv', 'w', newline='') as final_file:
    write = csv.writer(final_file, delimiter=',')
    write.writerow(['no', 'id', 'surname', 'name', 'rating'])
    for i, row in enumerate(ans_part, start=1):
        row.insert(0, i)
        write.writerow(row)
