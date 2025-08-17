import os
import zipfile
import shutil
import json
ans = {}
with zipfile.ZipFile('hh.zip') as zip_file:
    for file in zip_file.infolist():
        if '.csv' in file.filename:
            zip_file.extract(file.filename, 'hh1')
for file in os.listdir('hh1/hh'):
    csv = open(f'hh1/hh/{file}').readlines()
    for line in csv:
        line = line.rstrip().split(';')
        if line[1] != 'vacancy':
            line_2 = int(line[2])
            if line[1] not in ans:
                ans[line[1]] = ['.'.join([line[2], file, line[3]])]
            elif int(ans[line[1]][0].split('.')[-1]) / int(ans[line[1]][0].split('.')[0]) == int(line[3]) / line_2:
                ans[line[1]].append('.'.join([line[2], file, line[3]]))
            elif int(ans[line[1]][0].split('.')[-1]) / int(ans[line[1]][0].split('.')[0]) < int(line[3]) / line_2:
                ans[line[1]] = ['.'.join([line[2], file, line[3]])]
for key, item in sorted(ans.items()):
    ans_line = []
    for line in item:
        ans_line.append(line.split('.')[1])
    ans[key] = ans_line
with open('report.json', 'w') as ans_file:
    json.dump(ans, ans_file)
shutil.rmtree('hh1')