import os
import random

DIR = 'C:\AllArtem\games\Screenshots'

count = len(os.listdir(DIR)) - 1
count_l = list(range(count))

for root, dirs, files in os.walk(DIR):
    if dirs == 'TEMP' or root[:-4] == 'TEMP':
        continue
    if count:
        for f in files:
            ext = os.path.splitext(f)[-1]
            try:
                i = random.randint(0, count - 1)
            except ValueError:
                i = 0
            num = count_l.pop(i)
            count -= 1
            new_path = os.path.join('TEMP', f"{num:06d}{ext}")
            os.rename(os.path.join(root, f), os.path.join(root, new_path))
            # print(os.path.join(root, new_path))

for root, dirs, files in os.walk(os.path.join(DIR, 'TEMP')):
    for f in files:
        os.rename(os.path.join(root, f), os.path.join(DIR, f))
        # print(os.path.join(root, f), os.path.join(DIR, f))