HEADS, TAILS = input("N, M: ").split()
HEADS, TAILS = int(HEADS), int(TAILS)

atack = 0
run = True
while TAILS:
    if TAILS == 1:
        TAILS = 2
        atack += 1
    TAILS -= 2
    HEADS += 1
    atack += 2
    
while HEADS:
    if HEADS == 1:
        atack = -1
        break
    HEADS -= 2
    atack += 2
    
print(atack)
    