<<<<<<< HEAD
with open("INPUT.txt", "r") as f:
    n, m = map(int, f.readline().split())
    matrix = [list(map(int, f.readline().split())) for _ in range(n)]
     
ships = [] 
for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            continue

        ship = [(i, j)]
        while ship:
            x, y = ship.pop()
            if x+1 < n and matrix[x+1][y]:
                ship.append((x+1, y))
                matrix[x+1][y] = 0
            if x-1 >= 0 and matrix[x-1][y]:
                ship.append((x-1, y))
                matrix[x-1][y] = 0
            if y+1 < m and matrix[x][y+1]:
                ship.append((x, y+1))
                matrix[x][y+1] = 0
            if y-1 >= 0 and matrix[x][y-1]:
                ship.append((x, y-1))
                matrix[x][y-1] = 0
            print(ship)

        ships.append(len(ship))
        print("-------------------")
            
with open("OUTPUT.TXT", "w") as f:
    f.write(str(len(ships)))    
        
print(str(len(ships)))
=======
with open("INPUT.txt", "r") as f:
    n, m = map(int, f.readline().split())
    matrix = [list(map(int, f.readline().split())) for _ in range(n)]
     
ships = [] 
for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            continue

        ship = [(i, j)]
        while ship:
            x, y = ship.pop()
            if x+1 < n and matrix[x+1][y]:
                ship.append((x+1, y))
                matrix[x+1][y] = 0
            if x-1 >= 0 and matrix[x-1][y]:
                ship.append((x-1, y))
                matrix[x-1][y] = 0
            if y+1 < m and matrix[x][y+1]:
                ship.append((x, y+1))
                matrix[x][y+1] = 0
            if y-1 >= 0 and matrix[x][y-1]:
                ship.append((x, y-1))
                matrix[x][y-1] = 0
            print(ship)

        ships.append(len(ship))
        print("-------------------")
            
with open("OUTPUT.TXT", "w") as f:
    f.write(str(len(ships)))    
        
print(str(len(ships)))
>>>>>>> d4a9429d8f2eeba9daf04fa2d85d8eb63d449416
                    