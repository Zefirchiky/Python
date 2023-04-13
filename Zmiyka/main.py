<<<<<<< HEAD
import random
import pygame
import time

pygame.init()

''' Можна змінювати '''
WIDTH, HEIGHT = 900, 500 #ТІЛЬКИ ЧИСЛА КРАТНІ 20
DIS = pygame.display.set_mode((WIDTH, HEIGHT)) #Окрім цього
pygame.display.set_caption("Змійка") #Назва гри

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 144
SPEED = 100 #Чим вище значення, тим повільніша змійка (стандарт 100)

FONT_SIZE = 15 #Розмір текста
sect_Size = 19 #Розмір секцій змійки
apple_size = 17 #Розмір яблук

''' !!! НЕ ЗМІНЮВАТИ !!! '''
moveX = 20
moveY = 0

colbg1 = WHITE
colbg2 = BLACK

napr = 2
apple_eat = 0
apple_score = 1
score_font = pygame.font.SysFont("bahnschrift", FONT_SIZE)
 
 
def your_score(score, tic, col):
    value = score_font.render("Яблук зібрано: " + str(score-1), True, col)
    DIS.blit(value, [50, 30])
    toc = time.perf_counter()
    value2 = score_font.render("Часу прожито: " + str(round(toc - tic, 1)) + "сек.", True, col)
    DIS.blit(value2, [50, 50])

def start_Zmiyka():
    '''Початкова змійка'''
    el1 = [WIDTH/2-sect_Size/2-2*sect_Size, HEIGHT/2-sect_Size/2]
    el2 = [WIDTH/2-sect_Size/2-sect_Size, HEIGHT/2-sect_Size/2]
    global zmiyka_Head
    global full_Zmiyka
    zmiyka_Head = [WIDTH/2-sect_Size/2, HEIGHT/2-sect_Size/2]
    full_Zmiyka = []
    full_Zmiyka.append(el1)
    full_Zmiyka.append(el2)
    full_Zmiyka.append(zmiyka_Head)

def zmiykaCr(colzm, eat):
    '''Рендерінг змійки'''
    if eat == 0:
        del full_Zmiyka[0]
    else:
        global apple_eat
        apple_eat = 0
    full_Zmiyka.append(zmiyka_Head)
    for i in full_Zmiyka:
        pygame.draw.rect(DIS, colzm, [i[0], i[1], sect_Size, sect_Size])
    pygame.display.update()
        
def move(keys, za_polem):
    global moveX
    global moveY
    global napr
    if keys[pygame.K_a] and napr != 2 and za_polem !=1: #left
        moveX = -20
        moveY = 0
        napr = 1
    elif keys[pygame.K_d] and napr != 1 and za_polem !=1: #right
        moveX = 20
        moveY = 0
        napr = 2
    elif keys[pygame.K_w] and napr != 4 and za_polem !=1: #up
        moveX = 0
        moveY = -20
        napr = 3
    elif keys[pygame.K_s] and napr != 3 and za_polem !=1: #down
        moveX = 0
        moveY = 20
        napr = 4
    global zmiyka_Head
    zmiyka_Head = []
    head_MoveX = full_Zmiyka[-1][0] + moveX
    head_MoveY = full_Zmiyka[-1][1] + moveY
    zmiyka_Head.append(head_MoveX)
    zmiyka_Head.append(head_MoveY)
    pygame.time.delay(int(round(SPEED)))
    
def apple():
    global center_apple
    zmiyka_center = []
    zmiyka_center.append(zmiyka_Head[0]+sect_Size/2)
    zmiyka_center.append(zmiyka_Head[1]+sect_Size/2)
    global colbg_1
    global colbg_2
    colbg_1 = colbg1
    colbg_2 = colbg2
    if zmiyka_center == center_apple:
        center_apple = [random.randint(1, WIDTH/20-1)*20-10, random.randint(1, HEIGHT/20-1)*20-10]
        global apple_eat
        apple_eat = 1
        global apple_score
        apple_score += 1
        if apple_score % 10 == 0:
            colbg_1, colbg_2 = colbg_2, colbg_1
    pygame.draw.circle(DIS, RED, center_apple, apple_size/2)

def dis_events(colbg): #Бекграунд
    DIS.fill(colbg)
    
    
def main():
    tic = time.perf_counter()
    clock = pygame.time.Clock()
    clock.tick(FPS)
    run = True
    start_Zmiyka()
    global center_apple
    center_apple = [random.randint(1, WIDTH/20-1)*20-10, random.randint(1, HEIGHT/20-1)*20-10]
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for i in full_Zmiyka[:-1]: #Самовбивство
            if i == zmiyka_Head:
                run = False
        za_polem = 0
        if zmiyka_Head[0] <= 0:
            za_polem += 1
            zmiyka_Head[0] += WIDTH+20
        elif zmiyka_Head[0] >= WIDTH:
            toc = time.perf_counter()
            print(toc - tic)
            print("----------------------")
            za_polem += 1
            zmiyka_Head[0] -= WIDTH+20
        elif zmiyka_Head[1] <= 0:
            za_polem += 1
            zmiyka_Head[1] += HEIGHT+20
        elif zmiyka_Head[1] >= HEIGHT:
            za_polem += 1
            zmiyka_Head[1] -= HEIGHT+20
        keys_pressed = pygame.key.get_pressed()
        apple()
        global colbg1
        global colbg2
        colbg1 = colbg_1
        colbg2 = colbg_2
        your_score(apple_score, tic, colbg1)
        move(keys_pressed, za_polem)
        zmiykaCr(colbg_1, apple_eat)
        dis_events(colbg_2)
        
        
    pygame.quit()
    
if __name__ == "__main__":
=======
import random
import pygame
import time

pygame.init()

''' Можна змінювати '''
WIDTH, HEIGHT = 900, 500 #ТІЛЬКИ ЧИСЛА КРАТНІ 20
DIS = pygame.display.set_mode((WIDTH, HEIGHT)) #Окрім цього
pygame.display.set_caption("Змійка") #Назва гри

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 144
SPEED = 100 #Чим вище значення, тим повільніша змійка (стандарт 100)

FONT_SIZE = 15 #Розмір текста
sect_Size = 19 #Розмір секцій змійки
apple_size = 17 #Розмір яблук

''' !!! НЕ ЗМІНЮВАТИ !!! '''
moveX = 20
moveY = 0

colbg1 = WHITE
colbg2 = BLACK

napr = 2
apple_eat = 0
apple_score = 1
score_font = pygame.font.SysFont("bahnschrift", FONT_SIZE)
 
 
def your_score(score, tic, col):
    value = score_font.render("Яблук зібрано: " + str(score-1), True, col)
    DIS.blit(value, [50, 30])
    toc = time.perf_counter()
    value2 = score_font.render("Часу прожито: " + str(round(toc - tic, 1)) + "сек.", True, col)
    DIS.blit(value2, [50, 50])

def start_Zmiyka():
    '''Початкова змійка'''
    el1 = [WIDTH/2-sect_Size/2-2*sect_Size, HEIGHT/2-sect_Size/2]
    el2 = [WIDTH/2-sect_Size/2-sect_Size, HEIGHT/2-sect_Size/2]
    global zmiyka_Head
    global full_Zmiyka
    zmiyka_Head = [WIDTH/2-sect_Size/2, HEIGHT/2-sect_Size/2]
    full_Zmiyka = []
    full_Zmiyka.append(el1)
    full_Zmiyka.append(el2)
    full_Zmiyka.append(zmiyka_Head)

def zmiykaCr(colzm, eat):
    '''Рендерінг змійки'''
    if eat == 0:
        del full_Zmiyka[0]
    else:
        global apple_eat
        apple_eat = 0
    full_Zmiyka.append(zmiyka_Head)
    for i in full_Zmiyka:
        pygame.draw.rect(DIS, colzm, [i[0], i[1], sect_Size, sect_Size])
    pygame.display.update()
        
def move(keys, za_polem):
    global moveX
    global moveY
    global napr
    if keys[pygame.K_a] and napr != 2 and za_polem !=1: #left
        moveX = -20
        moveY = 0
        napr = 1
    elif keys[pygame.K_d] and napr != 1 and za_polem !=1: #right
        moveX = 20
        moveY = 0
        napr = 2
    elif keys[pygame.K_w] and napr != 4 and za_polem !=1: #up
        moveX = 0
        moveY = -20
        napr = 3
    elif keys[pygame.K_s] and napr != 3 and za_polem !=1: #down
        moveX = 0
        moveY = 20
        napr = 4
    global zmiyka_Head
    zmiyka_Head = []
    head_MoveX = full_Zmiyka[-1][0] + moveX
    head_MoveY = full_Zmiyka[-1][1] + moveY
    zmiyka_Head.append(head_MoveX)
    zmiyka_Head.append(head_MoveY)
    pygame.time.delay(int(round(SPEED)))
    
def apple():
    global center_apple
    zmiyka_center = []
    zmiyka_center.append(zmiyka_Head[0]+sect_Size/2)
    zmiyka_center.append(zmiyka_Head[1]+sect_Size/2)
    global colbg_1
    global colbg_2
    colbg_1 = colbg1
    colbg_2 = colbg2
    if zmiyka_center == center_apple:
        center_apple = [random.randint(1, WIDTH/20-1)*20-10, random.randint(1, HEIGHT/20-1)*20-10]
        global apple_eat
        apple_eat = 1
        global apple_score
        apple_score += 1
        if apple_score % 10 == 0:
            colbg_1, colbg_2 = colbg_2, colbg_1
    pygame.draw.circle(DIS, RED, center_apple, apple_size/2)

def dis_events(colbg): #Бекграунд
    DIS.fill(colbg)
    
    
def main():
    tic = time.perf_counter()
    clock = pygame.time.Clock()
    clock.tick(FPS)
    run = True
    start_Zmiyka()
    global center_apple
    center_apple = [random.randint(1, WIDTH/20-1)*20-10, random.randint(1, HEIGHT/20-1)*20-10]
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for i in full_Zmiyka[:-1]: #Самовбивство
            if i == zmiyka_Head:
                run = False
        za_polem = 0
        if zmiyka_Head[0] <= 0:
            za_polem += 1
            zmiyka_Head[0] += WIDTH+20
        elif zmiyka_Head[0] >= WIDTH:
            toc = time.perf_counter()
            print(toc - tic)
            print("----------------------")
            za_polem += 1
            zmiyka_Head[0] -= WIDTH+20
        elif zmiyka_Head[1] <= 0:
            za_polem += 1
            zmiyka_Head[1] += HEIGHT+20
        elif zmiyka_Head[1] >= HEIGHT:
            za_polem += 1
            zmiyka_Head[1] -= HEIGHT+20
        keys_pressed = pygame.key.get_pressed()
        apple()
        global colbg1
        global colbg2
        colbg1 = colbg_1
        colbg2 = colbg_2
        your_score(apple_score, tic, colbg1)
        move(keys_pressed, za_polem)
        zmiykaCr(colbg_1, apple_eat)
        dis_events(colbg_2)
        
        
    pygame.quit()
    
if __name__ == "__main__":
>>>>>>> d4a9429d8f2eeba9daf04fa2d85d8eb63d449416
    main()