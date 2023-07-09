import random
import time

#pip install pygame --pre

import pygame
pygame.init() #инициализация модуля pygame

#В игре используется палитра цвет RGB (Red Green Blue)
blue = (0,0,255) #код синего цвета
red = (255, 0, 0) #код красного цвета
white = (255, 255, 255) #код белого цвета
purp = (255, 0, 255)
black = (0,0,0)
dis = pygame.display.set_mode((800, 600)) #создали игровое окно размером 800 на 600 пикселей
pygame.display.set_caption('Змейка') #подпись игрового окна

game_over = False #флажок проигрыша. Если он в положении True, то игра окончена

window_size = pygame.display.get_window_size() #запоминаю размеры экрана

#Координаты змейки:
x_1 = 100 #координата по горизонтали
y_1 = 400 #по вертикали
x_1_change = 0 #на сколько пикселей сдвигается змейка (влево-вправо)
y_1_change = 0 #на сколько пикселей сдвигается змейка (вниз-вверх)

#Координаты яблока:
apple_x = random.randrange(0,window_size[0],10)
apple_y = random.randrange(0,window_size[1],10)

blok_x = random.randrange(50,window_size[0]-50,1)
blok_y = random.randrange(50,window_size[1]-50,1)

game_over_sound = pygame.mixer.Sound('Game_over.mp3')
eating_sound = pygame.mixer.Sound('apple_biting.mp3')
blok_sound = pygame.mixer.Sound('udar.mp3')

#Объявляем переменную clock (объект clock), через которую будем отслеживать время в игре
clock = pygame.time.Clock()

shake_spisok = []
Dlina_zmei = 1

width_shake = 10

speed_shake = 30
speed_ = speed_shake

score = 0 #объявляем счетчик очков

font = pygame.font.Font(None,36) #font - объект класса Font, шрифт 36 размера

# Координаты препятствий:
wall = []
for i in range(6):
    wall_x = random.randrange(0,window_size[0],10)
    wall_y = random.randrange(0,window_size[1],10)
    wall.append((wall_x, wall_y))
# Функция змейки:
def shake(width_shake,shake_spisok):
    for x in shake_spisok:
        pygame.draw.rect(dis,black, [x[0], x[1], width_shake, width_shake])

while not game_over: #начало основного цикла игры. Пока True, игра продолжается
    for event in pygame.event.get(): #цикл обработки событий
        if event.type == pygame.QUIT: #проверяем, не является ли текущее событие выходом из игры
            game_over = True
        if event.type == pygame.KEYDOWN: #задаем вопрос, не нажата ли какая-то клавиша
            if event.key == pygame.K_LEFT: #если нажата клавиша стрелка влево
                x_1_change = -10 #змейка будет ползти влево на 10 пикселей каждый фрейм игры
                y_1_change = 0 #в таком случае, вверх или влево ползти не нужно
            if event.key == pygame.K_RIGHT:
                x_1_change = 10 #змейка будет ползти вправо на 10 пикселей каждый фрейм игры
                y_1_change = 0
            if event.key == pygame.K_UP:
                y_1_change = -10 #змейка будет ползти вверх на 10 пикселей каждый фрейм игры
                x_1_change = 0
            if event.key == pygame.K_DOWN:
                y_1_change = 10 #змейка будет ползти вниз на 10 пикселей каждый фрейм игры
                x_1_change = 0

    if x_1 >= window_size[0] or y_1 >= window_size[1] or x_1 <= 0 or y_1 <= 0:
        game_over_sound.play()
        time.sleep(2)
        game_over = True

    x_1 += x_1_change #изменение фактических координат змейки
    y_1 += y_1_change

    time_elapsed = pygame.time.get_ticks()//1000

    dis.fill(white) #заполняю экран белым цветом, чтобы очистить всё, что до этого там находилось
    shake(width_shake, shake_spisok)
    nadpis = font.render('Очки: ' + str(score),True,red) #создали переменную nadpis, которая хранит надпись
    nadpis_speed = font.render('Скорость: '+str(speed_), True, purp)
    nadpis_cloc = font.render('Время: ' + str(time_elapsed), True, black)
    dis.blit(nadpis,(10,10))
    dis.blit(nadpis_speed, (5, 25))
    dis.blit(nadpis_cloc, (5, 50))

    pygame.draw.rect(dis,blue,[x_1,y_1,10,10])  #отрисовка прямоугольника синего цвета на игровом дисплее
    pygame.draw.rect(dis, black, [blok_x, blok_y, 30, 30])
    pygame.draw.rect(dis, red, [apple_x, apple_y, 10, 10]) #отрисовка яблока
    pygame.display.update() #обновление экрана для отображения изменений

    if x_1 in range(apple_x-5, apple_x+5,1) and y_1 in range(apple_y-5, apple_y+5,1):
        eating_sound.play()
        print('Съел!')
        apple_x = random.randrange(50, window_size[0]-50, 1)
        apple_y = random.randrange(50, window_size[1]-50, 1)
        if apple_x != blok_x and blok_x != x_1_change:
            blok_x = random.randrange(50, window_size[0]-50, 1)
        if apple_y != blok_y and blok_y != y_1_change:
            blok_y = random.randrange(50, window_size[1]-50, 1)
        score += 1
        speed_shake += 1.5
        speed_ = round(speed_shake,1)
        Dlina_zmei += 1

    shake_Head = []
    shake_spisok.append((x_1, y_1))
    if len(shake_spisok) > Dlina_zmei:
        del shake_spisok[0]
    for x in shake_spisok[:-1]:
        if x == (x_1,y_1):
            game_over_sound.play()
            time.sleep(2)
            game_over = True

    clock.tick(5) #ограничение кадров в секунду (фреймов)
pygame = quit()
quit()

