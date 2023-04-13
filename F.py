<<<<<<< HEAD
while 1:
    n=input("Символ:")
    k=len(n)
    if k<=6:
        k=round(6/k)
        print(k)
    else:
        k=1
        u=len(n)-6
        n=n[:-u]
    for i in range(3):
        print(n*k*3)
    for i in range(3):
        print(n*k)
    for i in range(3):
        print(n*k*2)
    for i in range(6):
        print(n*k)
=======
while 1:
    n=input("Символ:")
    k=len(n)
    if k<=6:
        k=round(6/k)
        print(k)
    else:
        k=1
        u=len(n)-6
        n=n[:-u]
    for i in range(3):
        print(n*k*3)
    for i in range(3):
        print(n*k)
    for i in range(3):
        print(n*k*2)
    for i in range(6):
        print(n*k)
>>>>>>> d4a9429d8f2eeba9daf04fa2d85d8eb63d449416
