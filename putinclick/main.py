import sys
import sqlite3
import random
import pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

FPS = 60
width = 480
height = 640
display = pygame.display.set_mode((width, height))
black = pygame.Surface((500,700))
black.fill((159,154,150))
pygame.display.set_caption("PutinClick")
clock = pygame.time.Clock()
font = pygame.font.Font("res\\Laptev_Brush.otf",28)
font1 = pygame.font.Font("res\\Laptev_Brush.otf",30)
fontm = pygame.font.Font("res\\roboto.ttf",22)
fontsave = pygame.font.Font("res\\roboto.ttf",19)
perehod = -9
sound = 1
vol = 0.5

money1 = pygame.mixer.Sound("res\\money1.wav")
money1.set_volume(vol)
money2 = pygame.mixer.Sound("res\\money2.wav")
money2.set_volume(vol)
money3 = pygame.mixer.Sound("res\\money3.wav")
money3.set_volume(vol)
money4 = pygame.mixer.Sound("res\\money4.wav")
money4.set_volume(vol)
buy = pygame.mixer.Sound("res\\buy.wav")
buy.set_volume(vol)
wasted = pygame.mixer.Sound("res\\wasted.wav")
wasted.set_volume(vol)

currentsave = 0

menu0 = pygame.image.load("res\\menu-main.jpg")
menu1 = pygame.image.load("res\\menu-main-1.jpg")
menu2 = pygame.image.load("res\\menu-main-2.jpg")
menu3 = pygame.image.load("res\\menu-main-3.jpg")

about0 = pygame.image.load("res\\about0.jpg")
about1 = pygame.image.load("res\\about1.jpg")

game1_0sound = pygame.image.load("res\\1.jpg")
game1_0nosound = pygame.image.load("res\\2.jpg")
game1backsound = pygame.image.load("res\\3.jpg")
game1backnosound = pygame.image.load("res\\4.jpg")
game1_2sound = pygame.image.load("res\\5.jpg")
game1_2nosound = pygame.image.load("res\\6.jpg")
game1_3sound = pygame.image.load("res\\7.jpg")
game1_3nosound = pygame.image.load("res\\8.jpg")
game1clicksound = pygame.image.load("res\\9.jpg")
game1clicknosound = pygame.image.load("res\\10.jpg")

game3_0 = pygame.image.load("res\\menu-stonks.jpg")
game3_back = pygame.image.load("res\\menu-stonks1.jpg")
game3_png = pygame.image.load("res\\1menu-stonks.png")
game3_pngback = pygame.image.load("res\\2menu-stonks1.png")

game2_0 = pygame.image.load("res\\menu-info1.jpg")
game2_back = pygame.image.load("res\\menu-info2.jpg")

loss0 = pygame.image.load("res\\menu-lose.jpg")
loss1 = pygame.image.load("res\\menu-lose1.jpg")

upgrade1_0 = pygame.image.load("res\\upgrade1_0.jpg")
upgrade1_1 = pygame.image.load("res\\upgrade1_1.jpg")
upgrade2_0 = pygame.image.load("res\\upgrade2_0.jpg")
upgrade2_1 = pygame.image.load("res\\upgrade2_1.jpg")
upgrade3_0 = pygame.image.load("res\\upgrade3_0.jpg")
upgrade3_1 = pygame.image.load("res\\upgrade3_1.jpg")
upgrade4_0 = pygame.image.load("res\\upgrade4_0.jpg")
upgrade4_1 = pygame.image.load("res\\upgrade4_1.jpg")
upgrade5_0 = pygame.image.load("res\\upgrade5_0.jpg")
upgrade5_1 = pygame.image.load("res\\upgrade5_1.jpg")
upgradewarn = pygame.image.load("res\\upgradewarn.jpg")

saves0 = pygame.image.load("res\\saves0.png")
saves1 = pygame.image.load("res\\saves1.png")
sgame1 = pygame.image.load("res\\game1.png")
sgame2 = pygame.image.load("res\\game2.png")
sgame3 = pygame.image.load("res\\game3.png")

def menu():
    global currentsave, sound, money, kf, click, cmoney, perehod, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5

    randfraza = random.randint(1, 9)
    if randfraza == 1:
        fraza = font.render(("Деньги не зло - зло так быстро не кончается"), True, (159, 154, 150))
    else:
        if randfraza == 2:
            fraza = font.render(("Хорошее не купишь дешево"), True, (159, 154, 150))
        else:
            if randfraza == 3:
                fraza = font.render(("На кукиш ничего не купишь"), True, (159, 154, 150))
            else:
                if randfraza == 4:
                    fraza = font.render(("Главное не деньги, главное - их количество"), True, (159, 154, 150))
                else:
                    if randfraza == 5:
                        fraza = font.render(("Время - деньги"), True, (159, 154, 150))
                    else:
                        if randfraza == 6:
                            fraza = font.render(("Монета карман не тянет"), True, (159, 154, 150))
                        else:
                            if randfraza == 7:
                                fraza = font.render(("Денег наживёшь - без нужды проживёшь"), True, (159, 154, 150))
                            else:
                                if randfraza == 8:
                                    fraza = font.render(("После Бога - деньги первые"), True, (159, 154, 150))
                                else:
                                    fraza = font.render(("Деньгам - время, потехе - час"), True, (159, 154, 150))
    fraza_rect = fraza.get_rect(center=(240, 617))

    for a in range(255, 0, perehod):
        display.blit(menu0, (0, 0))
        display.blit(fraza, fraza_rect)
        black.set_alpha(a)
        display.blit(black, (-10, -10))
        pygame.display.update()
        clock.tick(FPS)

    if perehod != -18:
        perehod = -18

    events = pygame.event.get()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos()
        if 28 <= mouse[0] <= 244 and 145 <= mouse[1] <= 184:
            display.blit(menu1, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        display.blit(menu1, (0, 0))
                        display.blit(fraza, fraza_rect)
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    saves()
        elif 28 <= mouse[0] <= 244 and 203 <= mouse[1] <= 241:
            display.blit(menu2, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        display.blit(menu2, (0, 0))
                        display.blit(fraza, fraza_rect)
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    about()
        elif 28 <= mouse[0] <= 244 and 260 <= mouse[1] <= 298:
            display.blit(menu3, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        display.blit(menu3, (0, 0))
                        display.blit(fraza, fraza_rect)
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    pygame.quit()
                    sys.exit()
        else:
            display.blit(menu0, (0, 0))

        display.blit(fraza, fraza_rect)

        pygame.display.update()
        clock.tick(FPS)

def saves():
    global currentsave, sound, money, kf, click, cmoney, perehod, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5

    with sqlite3.connect("res\\database.db") as db:
        cursor = db.cursor()
        command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
        cursor.execute(command)
        command = """ SELECT * FROM saves """
        cursor.execute(command)
        db.commit()

    save1exists = 0
    save2exists = 0
    save3exists = 0
    for res in cursor:
        if res[0] == 1:
            save1exists = 1
            m1text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
            cm1text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
        if res[0] == 2:
            save2exists = 1
            m2text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
            cm2text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
        if res[0] == 3:
            save3exists = 1
            m3text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
            cm3text = fontsave.render(str(round(res[3])), True, (37, 32, 29))

    for a in range(255, 0, -18):
        display.blit(saves0, (0, 0))
        if save1exists == 1:
            display.blit(sgame1, (41, 145))
            display.blit(cm1text, (91, 204))
            display.blit(m1text, (212, 204))
        if save2exists == 1:
            display.blit(sgame2, (41, 279))
            display.blit(cm2text, (91, 338))
            display.blit(m2text, (212, 338))
        if save3exists == 1:
            display.blit(sgame3, (41, 412))
            display.blit(cm3text, (91, 471))
            display.blit(m3text, (212, 471))
        black.set_alpha(a)
        display.blit(black, (-10, -10))
        pygame.display.update()
        clock.tick(FPS)

    events = pygame.event.get()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos()
        if 0 <= mouse[0] <= 480 and 595 <= mouse[1] <= 640:
            display.blit(saves1, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    with sqlite3.connect("res\\database.db") as db:
                        cursor = db.cursor()
                        command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
                        cursor.execute(command)
                        command = """ SELECT * FROM saves """
                        cursor.execute(command)
                        db.commit()

                    save1exists = 0
                    save2exists = 0
                    save3exists = 0
                    for res in cursor:
                        if res[0] == 1:
                            save1exists = 1
                            m1text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                            cm1text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                        if res[0] == 2:
                            save2exists = 1
                            m2text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                            cm2text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                        if res[0] == 3:
                            save3exists = 1
                            m3text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                            cm3text = fontsave.render(str(round(res[3])), True, (37, 32, 29))

                    for a in range(0, 256, 18):
                        display.blit(saves1, (0, 0))
                        if save1exists == 1:
                            display.blit(sgame1, (41, 145))
                            display.blit(cm1text, (91, 204))
                            display.blit(m1text, (212, 204))
                        if save2exists == 1:
                            display.blit(sgame2, (41, 279))
                            display.blit(cm2text, (91, 338))
                            display.blit(m2text, (212, 338))
                        if save3exists == 1:
                            display.blit(sgame3, (41, 412))
                            display.blit(cm3text, (91, 471))
                            display.blit(m3text, (212, 471))
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    menu()
        else:
            display.blit(saves0, (0, 0))

        with sqlite3.connect("res\\database.db") as db:
            cursor = db.cursor()
            command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
            cursor.execute(command)
            command = """ SELECT * FROM saves """
            cursor.execute(command)
            db.commit()

        save1exists = 0
        save2exists = 0
        save3exists = 0
        for res in cursor:
            if res[0] == 1:
                save1exists = 1
                display.blit(sgame1, (41, 145))
                mtext = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                cmtext = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                display.blit(cmtext, (91, 204))
                display.blit(mtext, (212, 204))
            if res[0] == 2:
                save2exists = 1
                display.blit(sgame2, (41, 279))
                mtext = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                cmtext = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                display.blit(cmtext, (91, 338))
                display.blit(mtext, (212, 338))
            if res[0] == 3:
                save3exists = 1
                display.blit(sgame3, (41, 412))
                mtext = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                cmtext = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                display.blit(cmtext, (91, 471))
                display.blit(mtext, (212, 471))

        if 41 <= mouse[0] <= 439 and 145 <= mouse[1] <= 245:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    currentsave = 1
                    if save1exists == 0:
                        with sqlite3.connect("res\\database.db") as db:
                            cursor = db.cursor()
                            command = """ INSERT INTO saves (id, kf, money, cmoney, click, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5) VALUES(1, 1, 0, 0, 10, 0, 0, 0, 0, 0, 0) """
                            cursor.execute(command)
                            db.commit()
                        kf = 1
                        money = 0
                        cmoney = 0
                        click = 10
                        result = 0
                        upgrade1 = 0
                        upgrade2 = 0
                        upgrade3 = 0
                        upgrade4 = 0
                        upgrade5 = 0
                        with sqlite3.connect("res\\database.db") as db:
                            cursor = db.cursor()
                            command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
                            cursor.execute(command)
                            command = """ SELECT * FROM saves """
                            cursor.execute(command)
                            db.commit()

                        save2exists = 0
                        save3exists = 0
                        for res in cursor:
                            if res[0] == 2:
                                save2exists = 1
                                m2text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                cm2text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                            if res[0] == 3:
                                save3exists = 1
                                m3text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                cm3text = fontsave.render(str(round(res[3])), True, (37, 32, 29))

                        for a in range(0, 256, 18):
                            display.blit(saves0, (0, 0))
                            if save2exists == 1:
                                display.blit(sgame2, (41, 279))
                                display.blit(cm2text, (91, 338))
                                display.blit(m2text, (212, 338))
                            if save3exists == 1:
                                display.blit(sgame3, (41, 412))
                                display.blit(cm3text, (91, 471))
                                display.blit(m3text, (212, 471))
                            black.set_alpha(a)
                            display.blit(black, (-10, -10))
                            pygame.display.update()
                            clock.tick(FPS)
                        game1()
                    else:
                        if 41 <= mouse[0] <= 326 and 145 <= mouse[1] <= 245:
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ SELECT * FROM saves WHERE id = 1 """
                                cursor.execute(command)
                                db.commit()
                            savestart = cursor.fetchone()
                            kf = savestart[1]
                            money = savestart[2]
                            cmoney = savestart[3]
                            click = savestart[4]
                            result = savestart[5]
                            upgrade1 = savestart[6]
                            upgrade2 = savestart[7]
                            upgrade3 = savestart[8]
                            upgrade4 = savestart[9]
                            upgrade5 = savestart[10]
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
                                cursor.execute(command)
                                command = """ SELECT * FROM saves """
                                cursor.execute(command)
                                db.commit()

                            save1exists = 0
                            save2exists = 0
                            save3exists = 0
                            for res in cursor:
                                if res[0] == 1:
                                    save1exists = 1
                                    m1text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm1text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                                if res[0] == 2:
                                    save2exists = 1
                                    m2text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm2text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                                if res[0] == 3:
                                    save3exists = 1
                                    m3text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm3text = fontsave.render(str(round(res[3])), True, (37, 32, 29))

                            for a in range(0, 256, 18):
                                display.blit(saves0, (0, 0))
                                if save1exists == 1:
                                    display.blit(sgame1, (41, 145))
                                    display.blit(cm1text, (91, 204))
                                    display.blit(m1text, (212, 204))
                                if save2exists == 1:
                                    display.blit(sgame2, (41, 279))
                                    display.blit(cm2text, (91, 338))
                                    display.blit(m2text, (212, 338))
                                if save3exists == 1:
                                    display.blit(sgame3, (41, 412))
                                    display.blit(cm3text, (91, 471))
                                    display.blit(m3text, (212, 471))
                                black.set_alpha(a)
                                display.blit(black, (-10, -10))
                                pygame.display.update()
                                clock.tick(FPS)
                            game1()
                        if 340 <= mouse[0] <= 439 and 145 <= mouse[1] <= 245:
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ DELETE FROM saves WHERE id = 1 """
                                cursor.execute(command)
                                db.commit()

        if 41 <= mouse[0] <= 439 and 279 <= mouse[1] <= 379:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    currentsave = 2
                    if save2exists == 0:
                        with sqlite3.connect("res\\database.db") as db:
                            cursor = db.cursor()
                            command = """ INSERT INTO saves (id, kf, money, cmoney, click, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5) VALUES(2, 1, 0, 0, 10, 0, 0, 0, 0, 0, 0) """
                            cursor.execute(command)
                            db.commit()
                        kf = 1
                        money = 0
                        cmoney = 0
                        click = 10
                        result = 0
                        upgrade1 = 0
                        upgrade2 = 0
                        upgrade3 = 0
                        upgrade4 = 0
                        upgrade5 = 0
                        with sqlite3.connect("res\\database.db") as db:
                            cursor = db.cursor()
                            command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
                            cursor.execute(command)
                            command = """ SELECT * FROM saves """
                            cursor.execute(command)
                            db.commit()

                        save1exists = 0
                        save3exists = 0
                        for res in cursor:
                            if res[0] == 1:
                                save1exists = 1
                                m1text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                cm1text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                            if res[0] == 3:
                                save3exists = 1
                                m3text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                cm3text = fontsave.render(str(round(res[3])), True, (37, 32, 29))

                        for a in range(0, 256, 18):
                            display.blit(saves0, (0, 0))
                            if save1exists == 1:
                                display.blit(sgame1, (41, 145))
                                display.blit(cm1text, (91, 204))
                                display.blit(m1text, (212, 204))
                            if save3exists == 1:
                                display.blit(sgame3, (41, 412))
                                display.blit(cm3text, (91, 471))
                                display.blit(m3text, (212, 471))
                            black.set_alpha(a)
                            display.blit(black, (-10, -10))
                            pygame.display.update()
                            clock.tick(FPS)
                        game1()
                    else:
                        if 41 <= mouse[0] <= 326 and 279 <= mouse[1] <= 379:
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ SELECT * FROM saves WHERE id = 2 """
                                cursor.execute(command)
                                db.commit()
                            savestart = cursor.fetchone()
                            kf = savestart[1]
                            money = savestart[2]
                            cmoney = savestart[3]
                            click = savestart[4]
                            result = savestart[5]
                            upgrade1 = savestart[6]
                            upgrade2 = savestart[7]
                            upgrade3 = savestart[8]
                            upgrade4 = savestart[9]
                            upgrade5 = savestart[10]
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
                                cursor.execute(command)
                                command = """ SELECT * FROM saves """
                                cursor.execute(command)
                                db.commit()

                            save1exists = 0
                            save2exists = 0
                            save3exists = 0
                            for res in cursor:
                                if res[0] == 1:
                                    save1exists = 1
                                    m1text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm1text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                                if res[0] == 2:
                                    save2exists = 1
                                    m2text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm2text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                                if res[0] == 3:
                                    save3exists = 1
                                    m3text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm3text = fontsave.render(str(round(res[3])), True, (37, 32, 29))

                            for a in range(0, 256, 18):
                                display.blit(saves0, (0, 0))
                                if save1exists == 1:
                                    display.blit(sgame1, (41, 145))
                                    display.blit(cm1text, (91, 204))
                                    display.blit(m1text, (212, 204))
                                if save2exists == 1:
                                    display.blit(sgame2, (41, 279))
                                    display.blit(cm2text, (91, 338))
                                    display.blit(m2text, (212, 338))
                                if save3exists == 1:
                                    display.blit(sgame3, (41, 412))
                                    display.blit(cm3text, (91, 471))
                                    display.blit(m3text, (212, 471))
                                black.set_alpha(a)
                                display.blit(black, (-10, -10))
                                pygame.display.update()
                                clock.tick(FPS)
                            game1()
                        if 340 <= mouse[0] <= 439 and 279 <= mouse[1] <= 379:
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ DELETE FROM saves WHERE id = 2 """
                                cursor.execute(command)
                                db.commit()

        if 41 <= mouse[0] <= 439 and 412 <= mouse[1] <= 512:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    currentsave = 3
                    if save3exists == 0:
                        with sqlite3.connect("res\\database.db") as db:
                            cursor = db.cursor()
                            command = """ INSERT INTO saves (id, kf, money, cmoney, click, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5) VALUES(3, 1, 0, 0, 10, 0, 0, 0, 0, 0, 0) """
                            cursor.execute(command)
                            db.commit()
                        kf = 1
                        money = 0
                        cmoney = 0
                        click = 10
                        result = 0
                        upgrade1 = 0
                        upgrade2 = 0
                        upgrade3 = 0
                        upgrade4 = 0
                        upgrade5 = 0
                        with sqlite3.connect("res\\database.db") as db:
                            cursor = db.cursor()
                            command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
                            cursor.execute(command)
                            command = """ SELECT * FROM saves """
                            cursor.execute(command)
                            db.commit()

                        save1exists = 0
                        save2exists = 0
                        for res in cursor:
                            if res[0] == 1:
                                save1exists = 1
                                m1text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                cm1text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                            if res[0] == 2:
                                save2exists = 1
                                m2text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                cm2text = fontsave.render(str(round(res[3])), True, (37, 32, 29))

                        for a in range(0, 256, 18):
                            display.blit(saves0, (0, 0))
                            if save1exists == 1:
                                display.blit(sgame1, (41, 145))
                                display.blit(cm1text, (91, 204))
                                display.blit(m1text, (212, 204))
                            if save2exists == 1:
                                display.blit(sgame2, (41, 279))
                                display.blit(cm2text, (91, 338))
                                display.blit(m2text, (212, 338))
                            black.set_alpha(a)
                            display.blit(black, (-10, -10))
                            pygame.display.update()
                            clock.tick(FPS)
                        game1()
                    else:
                        if 41 <= mouse[0] <= 326 and 412 <= mouse[1] <= 512:
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ SELECT * FROM saves WHERE id = 3 """
                                cursor.execute(command)
                                db.commit()
                            savestart = cursor.fetchone()
                            kf = savestart[1]
                            money = savestart[2]
                            cmoney = savestart[3]
                            click = savestart[4]
                            result = savestart[5]
                            upgrade1 = savestart[6]
                            upgrade2 = savestart[7]
                            upgrade3 = savestart[8]
                            upgrade4 = savestart[9]
                            upgrade5 = savestart[10]
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ CREATE TABLE IF NOT EXISTS saves(id INTEGER, kf REAL, money REAL, cmoney REAL, click REAL, result REAL, upgrade1 INTEGER, upgrade2 INTEGER, upgrade3 INTEGER, upgrade4 INTEGER, upgrade5 INTEGER) """
                                cursor.execute(command)
                                command = """ SELECT * FROM saves """
                                cursor.execute(command)
                                db.commit()

                            save1exists = 0
                            save2exists = 0
                            save3exists = 0
                            for res in cursor:
                                if res[0] == 1:
                                    save1exists = 1
                                    m1text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm1text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                                if res[0] == 2:
                                    save2exists = 1
                                    m2text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm2text = fontsave.render(str(round(res[3])), True, (37, 32, 29))
                                if res[0] == 3:
                                    save3exists = 1
                                    m3text = fontsave.render(str(round(res[2])), True, (37, 32, 29))
                                    cm3text = fontsave.render(str(round(res[3])), True, (37, 32, 29))

                            for a in range(0, 256, 18):
                                display.blit(saves0, (0, 0))
                                if save1exists == 1:
                                    display.blit(sgame1, (41, 145))
                                    display.blit(cm1text, (91, 204))
                                    display.blit(m1text, (212, 204))
                                if save2exists == 1:
                                    display.blit(sgame2, (41, 279))
                                    display.blit(cm2text, (91, 338))
                                    display.blit(m2text, (212, 338))
                                if save3exists == 1:
                                    display.blit(sgame3, (41, 412))
                                    display.blit(cm3text, (91, 471))
                                    display.blit(m3text, (212, 471))
                                black.set_alpha(a)
                                display.blit(black, (-10, -10))
                                pygame.display.update()
                                clock.tick(FPS)
                            game1()
                        if 340 <= mouse[0] <= 439 and 412 <= mouse[1] <= 512:
                            with sqlite3.connect("res\\database.db") as db:
                                cursor = db.cursor()
                                command = """ DELETE FROM saves WHERE id = 3 """
                                cursor.execute(command)
                                db.commit()

        pygame.display.update()
        clock.tick(FPS)

def about():
    global currentsave, sound, money, kf, click, cmoney, perehod, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5

    for a in range(255, 0, -18):
        display.blit(about0, (0, 0))
        black.set_alpha(a)
        display.blit(black, (-10, -10))
        pygame.display.update()
        clock.tick(FPS)

    events = pygame.event.get()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos()
        if 0 <= mouse[0] <= 480 and 595 <= mouse[1] <= 640:
            display.blit(about1, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        display.blit(about1, (0, 0))
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    menu()
        else:
            display.blit(about0, (0, 0))

        pygame.display.update()
        clock.tick(FPS)

def game1():
    global currentsave, sound, money, kf, click, cmoney, perehod, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5

    randfraza = random.randint(1, 9)
    if randfraza == 1:
        fraza = font.render(("Деньги не зло - зло так быстро не кончается"), True, (159, 154, 150))
    else:
        if randfraza == 2:
            fraza = font.render(("Хорошее не купишь дешево"), True, (159, 154, 150))
        else:
            if randfraza == 3:
                fraza = font.render(("На кукиш ничего не купишь"), True, (159, 154, 150))
            else:
                if randfraza == 4:
                    fraza = font.render(("Главное не деньги, главное - их количество"), True, (159, 154, 150))
                else:
                    if randfraza == 5:
                        fraza = font.render(("Время - деньги"), True, (159, 154, 150))
                    else:
                        if randfraza == 6:
                            fraza = font.render(("Монета карман не тянет"), True, (159, 154, 150))
                        else:
                            if randfraza == 7:
                                fraza = font.render(("Денег наживёшь - без нужды проживёшь"), True, (159, 154, 150))
                            else:
                                if randfraza == 8:
                                    fraza = font.render(("После Бога - деньги первые"), True, (159, 154, 150))
                                else:
                                    fraza = font.render(("Деньгам - время, потехе - час"), True, (159, 154, 150))
    fraza_rect = fraza.get_rect(center=(240, 620))

    for a in range(255, 0, -18):
        kf += 0.03
        money += 0.1*kf
        if sound == 1:
            display.blit(game1_0sound, (0, 0))
        else:
            display.blit(game1_0nosound, (0, 0))
        mtext = fontm.render(str(round(money)), True, (159, 154 , 150))
        cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
        display.blit(cmtext, (100, 11))
        display.blit(mtext, (281, 11))
        display.blit(fraza, fraza_rect)
        black.set_alpha(a)
        display.blit(black, (-10, -10))
        pygame.display.update()
        clock.tick(FPS)

    events = pygame.event.get()

    while True:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                with sqlite3.connect("res\\database.db") as db:
                    cursor = db.cursor()
                    command = """ UPDATE saves SET kf = %s, money = %s, cmoney = %s, click = %s, result = %s, upgrade1 = %s, upgrade2 = %s, upgrade3 = %s, upgrade4 = %s, upgrade5 = %s WHERE id = %s """ % (kf, money, cmoney, click, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5, currentsave)
                    cursor.execute(command)
                    db.commit()
                pygame.quit()
                sys.exit()

        kf += 0.03
        money += 0.1*kf
        if money > 100000:
            if sound == 1:
                pygame.mixer.Sound.play(wasted)
            for a in range(0, 256, 18):
                if sound == 1:
                    display.blit(game1_0sound, (0, 0))
                else:
                    display.blit(game1_0nosound, (0, 0))
                mtext = fontm.render(str(round(money)), True, (159, 154, 150))
                cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
                display.blit(cmtext, (100, 11))
                display.blit(mtext, (281, 11))
                display.blit(fraza, fraza_rect)
                black.set_alpha(a)
                display.blit(black, (-10, -10))
                pygame.display.update()
                clock.tick(FPS)
            loss()

        if sound == 1:
            display.blit(game1_0sound, (0, 0))
        else:
            display.blit(game1_0nosound, (0, 0))

        mouse = pygame.mouse.get_pos()

        if 107 <= mouse[0] <= 180 and 64 <= mouse[1] <= 124:
            if sound == 1:
                display.blit(game1backsound, (0, 0))
            else:
                display.blit(game1backnosound, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        kf += 0.03
                        money += 0.1 * kf
                        if sound == 1:
                            display.blit(game1backsound, (0, 0))
                        else:
                            display.blit(game1backnosound, (0, 0))
                        mtext = fontm.render(str(round(money)), True, (159, 154, 150))
                        cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
                        display.blit(cmtext, (100, 11))
                        display.blit(mtext, (281, 11))
                        display.blit(fraza, fraza_rect)
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    with sqlite3.connect("res\\database.db") as db:
                        cursor = db.cursor()
                        command = """ UPDATE saves SET kf = %s, money = %s, cmoney = %s, click = %s, result = %s, upgrade1 = %s, upgrade2 = %s, upgrade3 = %s, upgrade4 = %s, upgrade5 = %s WHERE id = %s """ % (kf, money, cmoney, click, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5, currentsave)
                        cursor.execute(command)
                        db.commit()
                    menu()
        if 182 <= mouse[0] <= 300 and 64 <= mouse[1] <= 124:
            if sound == 1:
                display.blit(game1_2sound, (0, 0))
            else:
                display.blit(game1_2nosound, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        kf += 0.03
                        money += 0.1 * kf
                        if sound == 1:
                            display.blit(game1_2sound, (0, 0))
                        else:
                            display.blit(game1_2nosound, (0, 0))
                        mtext = fontm.render(str(round(money)), True, (159, 154, 150))
                        cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
                        display.blit(cmtext, (100, 11))
                        display.blit(mtext, (281, 11))
                        display.blit(fraza, fraza_rect)
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    game3()
        if 302 <= mouse[0] <= 397 and 64 <= mouse[1] <= 124:
            if sound == 1:
                display.blit(game1_3sound, (0, 0))
            else:
                display.blit(game1_3nosound, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        kf += 0.03
                        money += 0.1 * kf
                        if sound == 1:
                            display.blit(game1_3sound, (0, 0))
                        else:
                            display.blit(game1_3nosound, (0, 0))
                        mtext = fontm.render(str(round(money)), True, (159, 154, 150))
                        cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
                        display.blit(cmtext, (100, 11))
                        display.blit(mtext, (281, 11))
                        display.blit(fraza, fraza_rect)
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    game2()
        if 424 <= mouse[0] <= 480 and 0 <= mouse[1] <= 47:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sound == 1:
                        sound = 0
                    else:
                        sound = 1

        if 123 <= mouse[0] <= 361 and 489 <= mouse[1] <= 564:
            if sound == 1:
                display.blit(game1clicksound, (0, 0))
            else:
                display.blit(game1clicknosound, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sound == 1:
                        randmoney = random.randint(1,4)
                        if randmoney == 1:
                            pygame.mixer.Sound.play(money1)
                        else:
                            if randmoney == 2:
                                pygame.mixer.Sound.play(money2)
                            else:
                                if randmoney == 3:
                                    pygame.mixer.Sound.play(money3)
                                else:
                                    if randmoney == 4:
                                        pygame.mixer.Sound.play(money4)

                    cmoney += click * 0.1
                    result += click * 0.1
                    if money >= click:
                        money -= click
                    else:
                        money = 0

        mtext = fontm.render(str(round(money)), True, (159, 154 , 150))
        cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
        display.blit(cmtext, (100, 11))
        display.blit(mtext, (281, 11))
        display.blit(fraza, fraza_rect)

        pygame.display.update()
        clock.tick(FPS)

def game2():
    global currentsave, sound, money, kf, click, cmoney, perehod, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5

    for a in range(255, 0, -18):
        display.blit(game2_0, (0, 0))
        black.set_alpha(a)
        display.blit(black, (-10, -10))
        pygame.display.update()
        clock.tick(FPS)

    events = pygame.event.get()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                with sqlite3.connect("res\\database.db") as db:
                    cursor = db.cursor()
                    command = """ UPDATE saves SET kf = %s, money = %s, cmoney = %s, click = %s, result = %s, upgrade1 = %s, upgrade2 = %s, upgrade3 = %s, upgrade4 = %s, upgrade5 = %s WHERE id = %s """ % (kf, money, cmoney, click, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5, currentsave)
                    cursor.execute(command)
                    db.commit()
                pygame.quit()
                sys.exit()

        if money > 100000:
            if sound == 1:
                pygame.mixer.Sound.play(wasted)
            for a in range(0, 256, 18):
                display.blit(game2_0, (0, 0))
                black.set_alpha(a)
                display.blit(black, (-10, -10))
                pygame.display.update()
                clock.tick(FPS)
            loss()

        mouse = pygame.mouse.get_pos()
        if 0 <= mouse[0] <= 480 and 595 <= mouse[1] <= 640:
            display.blit(game2_back, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        display.blit(game2_back, (0, 0))
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    game1()
        else:
            display.blit(game2_0, (0, 0))

        pygame.display.update()
        clock.tick(FPS)

def game3():
    global currentsave, sound, money, kf, click, cmoney, perehod, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5

    scrollc = 0
    upgrade1c = 0
    upgrade2c = 0
    upgrade3c = 0
    upgrade4c = 0
    upgrade5c = 0
    scroll = 20

    for a in range(255, 0, -18):
        kf += 0.03
        money += 0.1*kf
        display.blit(game3_0, (0, 0))

        if 128 - scrollc * scroll > 18 and 128 - scrollc * scroll < 595:
            if upgrade1 == 0:
                display.blit(upgrade1_0, (41, 128 - scrollc * scroll))
            else:
                display.blit(upgrade1_1, (41, 128 - scrollc * scroll))
        if 238 - scrollc * scroll > 18 and 238 - scrollc * scroll < 595:
            if upgrade2 == 0:
                display.blit(upgrade2_0, (41, 238 - scrollc * scroll))
            else:
                display.blit(upgrade2_1, (41, 238 - scrollc * scroll))
        if 348 - scrollc * scroll > 18 and 348 - scrollc * scroll < 595:
            if upgrade3 == 0:
                display.blit(upgrade3_0, (41, 348 - scrollc * scroll))
            else:
                display.blit(upgrade3_1, (41, 348 - scrollc * scroll))
        if 458 - scrollc * scroll > 18 and 458 - scrollc * scroll < 595:
            if upgrade4 == 0:
                display.blit(upgrade4_0, (41, 458 - scrollc * scroll))
            else:
                display.blit(upgrade4_1, (41, 458 - scrollc * scroll))
        if 568 - scrollc * scroll > 18 and 568 - scrollc * scroll < 595:
            if upgrade5 == 0:
                display.blit(upgrade5_0, (41, 568 - scrollc * scroll))
            else:
                display.blit(upgrade5_1, (41, 568 - scrollc * scroll))

        display.blit(game3_png, (0, 0))

        mtext = fontm.render(str(round(money)), True, (159, 154, 150))
        cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
        display.blit(cmtext, (257, 604))
        display.blit(mtext, (378, 604))

        black.set_alpha(a)
        display.blit(black, (-10, -10))
        pygame.display.update()
        clock.tick(FPS)

    events = pygame.event.get()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                with sqlite3.connect("res\\database.db") as db:
                    cursor = db.cursor()
                    command = """ UPDATE saves SET kf = %s, money = %s, cmoney = %s, click = %s, result = %s, upgrade1 = %s, upgrade2 = %s, upgrade3 = %s, upgrade4 = %s, upgrade5 = %s WHERE id = %s """ % (kf, money, cmoney, click, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5, currentsave)
                    cursor.execute(command)
                    db.commit()
                pygame.quit()
                sys.exit()

        kf += 0.03
        money += 0.1*kf
        if money > 100000:
            if sound == 1:
                pygame.mixer.Sound.play(wasted)
            for a in range(0, 256, 18):
                display.blit(game3_0, (0, 0))

                if 128 - scrollc * scroll > 18 and 128 - scrollc * scroll < 595:
                    if upgrade1 == 0:
                        display.blit(upgrade1_0, (41, 128 - scrollc * scroll))
                    else:
                        display.blit(upgrade1_1, (41, 128 - scrollc * scroll))
                if 238 - scrollc * scroll > 18 and 238 - scrollc * scroll < 595:
                    if upgrade2 == 0:
                        display.blit(upgrade2_0, (41, 238 - scrollc * scroll))
                    else:
                        display.blit(upgrade2_1, (41, 238 - scrollc * scroll))
                if 348 - scrollc * scroll > 18 and 348 - scrollc * scroll < 595:
                    if upgrade3 == 0:
                        display.blit(upgrade3_0, (41, 348 - scrollc * scroll))
                    else:
                        display.blit(upgrade3_1, (41, 348 - scrollc * scroll))
                if 458 - scrollc * scroll > 18 and 458 - scrollc * scroll < 595:
                    if upgrade4 == 0:
                        display.blit(upgrade4_0, (41, 458 - scrollc * scroll))
                    else:
                        display.blit(upgrade4_1, (41, 458 - scrollc * scroll))
                if 568 - scrollc * scroll > 18 and 568 - scrollc * scroll < 595:
                    if upgrade5 == 0:
                        display.blit(upgrade5_0, (41, 568 - scrollc * scroll))
                    else:
                        display.blit(upgrade5_1, (41, 568 - scrollc * scroll))

                if upgrade1c > 0:
                    display.blit(upgradewarn, (41, 128 - scrollc * scroll))
                    upgrade1c -= 1
                if upgrade2c > 0:
                    display.blit(upgradewarn, (41, 238 - scrollc * scroll))
                    upgrade2c -= 1
                if upgrade3c > 0:
                    display.blit(upgradewarn, (41, 348 - scrollc * scroll))
                    upgrade3c -= 1
                if upgrade4c > 0:
                    display.blit(upgradewarn, (41, 458 - scrollc * scroll))
                    upgrade4c -= 1
                if upgrade5c > 0:
                    display.blit(upgradewarn, (41, 568 - scrollc * scroll))
                    upgrade5c -= 1

                display.blit(game3_png, (0, 0))

                mtext = fontm.render(str(round(money)), True, (159, 154, 150))
                cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
                display.blit(cmtext, (257, 604))
                display.blit(mtext, (378, 604))

                black.set_alpha(a)
                display.blit(black, (-10, -10))
                pygame.display.update()
                clock.tick(FPS)

            loss()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and scrollc < 4:
                scrollc += 1
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and scrollc > 0:
                scrollc -= 1


        mouse = pygame.mouse.get_pos()
        display.blit(game3_0, (0, 0))


        if 128 - scrollc * scroll > 18 and 128 - scrollc * scroll < 595:
            if upgrade1 == 0:
                display.blit(upgrade1_0, (41, 128 - scrollc * scroll))
            else:
                display.blit(upgrade1_1, (41, 128 - scrollc * scroll))
        if 238 - scrollc * scroll > 18 and 238 - scrollc * scroll < 595:
            if upgrade2 == 0:
                display.blit(upgrade2_0, (41, 238 - scrollc * scroll))
            else:
                display.blit(upgrade2_1, (41, 238 - scrollc * scroll))
        if 348 - scrollc * scroll > 18 and 348 - scrollc * scroll < 595:
            if upgrade3 == 0:
                display.blit(upgrade3_0, (41, 348 - scrollc * scroll))
            else:
                display.blit(upgrade3_1, (41, 348 - scrollc * scroll))
        if 458 - scrollc * scroll > 18 and 458 - scrollc * scroll < 595:
            if upgrade4 == 0:
                display.blit(upgrade4_0, (41, 458 - scrollc * scroll))
            else:
                display.blit(upgrade4_1, (41, 458 - scrollc * scroll))
        if 568 - scrollc * scroll > 18 and 568 - scrollc * scroll < 595:
            if upgrade5 == 0:
                display.blit(upgrade5_0, (41, 568 - scrollc * scroll))
            else:
                display.blit(upgrade5_1, (41, 568 - scrollc * scroll))

        if upgrade1 == 0:
            if 41 <= mouse[0] <= 439 and (128 - scrollc * scroll) <= mouse[1] <= (228 - scrollc * scroll) and 120 <= mouse[1] <= 594:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if cmoney >= 100:
                            if sound == 1:
                                pygame.mixer.Sound.play(buy)
                            cmoney -= 100
                            upgrade1 = 1
                            click += 20
                        else:
                            if upgrade1c <= 0:
                                upgrade1c = 90
            if upgrade1c > 0:
                display.blit(upgradewarn, (41, 128 - scrollc * scroll))
                upgrade1c -= 1
        if upgrade2 == 0:
            if 41 <= mouse[0] <= 439 and (238 - scrollc * scroll) <= mouse[1] <= (338 - scrollc * scroll) and 120 <= mouse[1] <= 594:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if cmoney >= 500:
                            if sound == 1:
                                pygame.mixer.Sound.play(buy)
                            cmoney -= 500
                            upgrade2 = 1
                            click += 100
                        else:
                            if upgrade2c <= 0:
                                upgrade2c = 90
            if upgrade2c > 0:
                display.blit(upgradewarn, (41, 238 - scrollc * scroll))
                upgrade2c -= 1
        if upgrade3 == 0:
            if 41 <= mouse[0] <= 439 and (348 - scrollc * scroll) <= mouse[1] <= (448 - scrollc * scroll) and 120 <= mouse[1] <= 594:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if cmoney >= 1000:
                            if sound == 1:
                                pygame.mixer.Sound.play(buy)
                            cmoney -= 1000
                            upgrade3 = 1
                            click += 200
                        else:
                            if upgrade3c <= 0:
                                upgrade3c = 90
            if upgrade3c > 0:
                display.blit(upgradewarn, (41, 348 - scrollc * scroll))
                upgrade3c -= 1
        if upgrade4 == 0:
            if 41 <= mouse[0] <= 439 and (458 - scrollc * scroll) <= mouse[1] <= (558 - scrollc * scroll) and 120 <= mouse[1] <= 594:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if cmoney >= 10000:
                            if sound == 1:
                                pygame.mixer.Sound.play(buy)
                            cmoney -= 10000
                            upgrade4 = 1
                            click += 1000
                        else:
                            if upgrade4c <= 0:
                                upgrade4c = 90
            if upgrade4c > 0:
                display.blit(upgradewarn, (41, 458 - scrollc * scroll))
                upgrade4c -= 1
        if upgrade5 == 0:
            if 41 <= mouse[0] <= 439 and (568 - scrollc * scroll) <= mouse[1] <= (668 - scrollc * scroll) and 120 <= mouse[1] <= 594:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if cmoney >= 30000:
                            if sound == 1:
                                pygame.mixer.Sound.play(buy)
                            cmoney -= 30000
                            upgrade5 = 1
                            click += 6000
                        else:
                            if upgrade5c <= 0:
                                upgrade5c = 90
            if upgrade5c > 0:
                display.blit(upgradewarn, (41, 568 - scrollc * scroll))
                upgrade5c -= 1

        if 0 <= mouse[0] <= 480 and 594 <= mouse[1] <= 640:
            display.blit(game3_pngback, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        kf += 0.03
                        money += 0.1 * kf
                        display.blit(game3_0, (0, 0))

                        if 128 - scrollc * scroll > 18 and 128 - scrollc * scroll < 595:
                            if upgrade1 == 0:
                                display.blit(upgrade1_0, (41, 128 - scrollc * scroll))
                            else:
                                display.blit(upgrade1_1, (41, 128 - scrollc * scroll))
                        if 238 - scrollc * scroll > 18 and 238 - scrollc * scroll < 595:
                            if upgrade2 == 0:
                                display.blit(upgrade2_0, (41, 238 - scrollc * scroll))
                            else:
                                display.blit(upgrade2_1, (41, 238 - scrollc * scroll))
                        if 348 - scrollc * scroll > 18 and 348 - scrollc * scroll < 595:
                            if upgrade3 == 0:
                                display.blit(upgrade3_0, (41, 348 - scrollc * scroll))
                            else:
                                display.blit(upgrade3_1, (41, 348 - scrollc * scroll))
                        if 458 - scrollc * scroll > 18 and 458 - scrollc * scroll < 595:
                            if upgrade4 == 0:
                                display.blit(upgrade4_0, (41, 458 - scrollc * scroll))
                            else:
                                display.blit(upgrade4_1, (41, 458 - scrollc * scroll))
                        if 568 - scrollc * scroll > 18 and 568 - scrollc * scroll < 595:
                            if upgrade5 == 0:
                                display.blit(upgrade5_0, (41, 568 - scrollc * scroll))
                            else:
                                display.blit(upgrade5_1, (41, 568 - scrollc * scroll))

                        if upgrade1c > 0:
                            display.blit(upgradewarn, (41, 128 - scrollc * scroll))
                            upgrade1c -= 1
                        if upgrade2c > 0:
                            display.blit(upgradewarn, (41, 238 - scrollc * scroll))
                            upgrade2c -= 1
                        if upgrade3c > 0:
                            display.blit(upgradewarn, (41, 348 - scrollc * scroll))
                            upgrade3c -= 1
                        if upgrade4c > 0:
                            display.blit(upgradewarn, (41, 458 - scrollc * scroll))
                            upgrade4c -= 1
                        if upgrade5c > 0:
                            display.blit(upgradewarn, (41, 568 - scrollc * scroll))
                            upgrade5c -= 1

                        display.blit(game3_pngback, (0, 0))

                        mtext = fontm.render(str(round(money)), True, (159, 154, 150))
                        cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
                        display.blit(cmtext, (257, 604))
                        display.blit(mtext, (378, 604))

                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)

                    game1()
        else:
            display.blit(game3_png, (0, 0))

        mtext = fontm.render(str(round(money)), True, (159, 154 , 150))
        cmtext = fontm.render(str(round(cmoney)), True, (159, 154, 150))
        display.blit(cmtext, (257, 604))
        display.blit(mtext, (378, 604))

        pygame.display.update()
        clock.tick(FPS)

def loss():
    global currentsave, sound, money, kf, click, cmoney, perehod, result, upgrade1, upgrade2, upgrade3, upgrade4, upgrade5

    resulttext = font1.render((" ".join([str(round(result)), "р."])), True, (159, 154, 150))
    result_rect = resulttext.get_rect(center=(240, 101))

    for a in range(255, 0, -18):
        display.blit(loss0, (0, 0))
        display.blit(resulttext, result_rect)
        black.set_alpha(a)
        display.blit(black, (-10, -10))
        pygame.display.update()
        clock.tick(FPS)

    with sqlite3.connect("res\\database.db") as db:
        cursor = db.cursor()
        command = """ DELETE FROM saves WHERE id = %s """ % currentsave
        cursor.execute(command)
        db.commit()

    events = pygame.event.get()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos()
        if 0 <= mouse[0] <= 480 and 595 <= mouse[1] <= 640:
            display.blit(loss1, (0, 0))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for a in range(0, 256, 18):
                        display.blit(loss1, (0, 0))
                        display.blit(resulttext, result_rect)
                        black.set_alpha(a)
                        display.blit(black, (-10, -10))
                        pygame.display.update()
                        clock.tick(FPS)
                    menu()
        else:
            display.blit(loss0, (0, 0))

        display.blit(resulttext, result_rect)

        pygame.display.update()
        clock.tick(FPS)


menu()