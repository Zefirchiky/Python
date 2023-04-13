<<<<<<< HEAD
with open("INPUT.txt", "r") as f:
    lines = f.readlines()
    time1 = lines[0].split(":")
    time_sleep = lines[1].split(":")
    
off_time = []
for i, num in enumerate(time1):
    off_time.append(int(num) + int(time_sleep[i]))

days = 0

while off_time[2] // 60:
    off_time[1] += 1
    off_time[2] -= 60
        
while off_time[1] // 60:
    off_time[0] += 1
    off_time[1] -= 60
        
while off_time[0] // 24:
    off_time[0] -= 24
    days += 1

with open("OUTPUT.txt", "w") as f:
    f.write(f"{off_time[0]}:{off_time[1]}:{off_time[2]}+{days}")
=======
with open("INPUT.txt", "r") as f:
    lines = f.readlines()
    time1 = lines[0].split(":")
    time_sleep = lines[1].split(":")
    
off_time = []
for i, num in enumerate(time1):
    off_time.append(int(num) + int(time_sleep[i]))

days = 0

while off_time[2] // 60:
    off_time[1] += 1
    off_time[2] -= 60
        
while off_time[1] // 60:
    off_time[0] += 1
    off_time[1] -= 60
        
while off_time[0] // 24:
    off_time[0] -= 24
    days += 1

with open("OUTPUT.txt", "w") as f:
    f.write(f"{off_time[0]}:{off_time[1]}:{off_time[2]}+{days}")
>>>>>>> d4a9429d8f2eeba9daf04fa2d85d8eb63d449416
print(f"{off_time[0]}:{off_time[1]}:{off_time[2]}+{days}")