import pygame
import os
import random
import time                                   

def check_input_exit():
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
                        

def display_text(win, text, positionX, positionY, size,R,G,B):    #Fonction texte
    font = pygame.font.SysFont("arial", size)                     #Police et taille
    font.set_bold(True)                                   
    text = font.render(text, True, (R, G, B), None)               #Couleur
    win.blit(text, (positionX, positionY))                        #Position du texte




def loading_picture():
    background1 = pygame.image.load("background/background1.png").convert_alpha()
    background1 = pygame.transform.scale(background1, (5000, 700))
    background2 = pygame.image.load("background/background2.png").convert_alpha()
    background3 = pygame.image.load("background/background3.png").convert_alpha()
    background4 = pygame.image.load("background/background4.png").convert_alpha()
    background4 = pygame.transform.scale(background4, (5000, 700))
    background5 = pygame.image.load("background/background5.png").convert_alpha()
    monster = pygame.image.load("monsters/skeleton/walk/walk1.png").convert_alpha()
    monster = pygame.transform.scale(monster, (200, 148)) 
    # background5 = pygame.transform.scale(background5, (5000, 700))


    
    paint = pygame.image.load("tableau.png.").convert_alpha()
    # paint = pygame.transform.scale(paint, (432, 270))

    road = pygame.image.load("road.png.").convert_alpha()

    return background1,background2,background3,background4,background5, paint, road,monster


def loading_player_sprite(position,dash):
    player = pygame.image.load("player/run/run"+str(position)+".png").convert_alpha()
    if position >= 12:
        position = 0
    player = pygame.transform.scale(player, (200, 148))    
    position += 1
    return position, player

def loading_player_attack(position,player,Vera,Combo):
    print ("Combo",Combo)
    if Combo == 1:
 
        player = pygame.image.load("player/attack/1attack"+str(position)+".png").convert_alpha()                 #affichage de sprites en condensé

        if position >= 15:
            player = pygame.image.load("player/attack/1attack5.png").convert_alpha()
            position = 0
            Vera = False
    #------------------------------------------------------------------------------------
    if Combo == 2:
        if position == 1:
            player = pygame.image.load("player/attack/2attack1.png").convert_alpha()
        elif position == 2:
            player = pygame.image.load("player/attack/2attack1.png").convert_alpha()
        elif position == 3:
            player = pygame.image.load("player/attack/2attack1.png").convert_alpha()
        elif position == 4:
            player = pygame.image.load("player/attack/2attack2.png").convert_alpha()                            #affichage de sprites sans condensé
        elif position == 5:
            player = pygame.image.load("player/attack/2attack2.png").convert_alpha()
        elif position == 6:
            player = pygame.image.load("player/attack/2attack2.png").convert_alpha()
        elif position == 7:  
            player = pygame.image.load("player/attack/2attack3.png").convert_alpha()           
        elif position == 8:
            player = pygame.image.load("player/attack/2attack3.png").convert_alpha()
        elif position == 9:
            player = pygame.image.load("player/attack/2attack3.png").convert_alpha()
        elif position == 10:
            player = pygame.image.load("player/attack/2attack4.png").convert_alpha()
        elif position == 11:
            player = pygame.image.load("player/attack/2attack4.png").convert_alpha()
        elif position == 12:
            player = pygame.image.load("player/attack/2attack4.png").convert_alpha()
        elif position == 13:
            player = pygame.image.load("player/attack/2attack5.png").convert_alpha()
        elif position == 14:
            player = pygame.image.load("player/attack/2attack5.png").convert_alpha()
        elif position == 15:
            player = pygame.image.load("player/attack/2attack5.png").convert_alpha()
        elif position == 16:
            player = pygame.image.load("player/attack/2attack6.png").convert_alpha()
        elif position == 17:
            player = pygame.image.load("player/attack/2attack6.png").convert_alpha()
        elif position >= 18:
            player = pygame.image.load("player/attack/2attack6.png").convert_alpha()
            position = 0
            Vera = False
    #-------------------------------------------------------------------------------
    if Combo == 3:
        if position == 1:
            player = pygame.image.load("player/attack/3attack1.png").convert_alpha()
        elif position == 2:
            player = pygame.image.load("player/attack/3attack1.png").convert_alpha()
        elif position == 3:
            player = pygame.image.load("player/attack/3attack1.png").convert_alpha()
        elif position == 4:
            player = pygame.image.load("player/attack/3attack2.png").convert_alpha()
        elif position == 5:
            player = pygame.image.load("player/attack/3attack2.png").convert_alpha()
        elif position == 6:
            player = pygame.image.load("player/attack/3attack2.png").convert_alpha()
        elif position == 7:  
            player = pygame.image.load("player/attack/3attack3.png").convert_alpha()           
        elif position == 8:
            player = pygame.image.load("player/attack/3attack3.png").convert_alpha()
        elif position == 9:
            player = pygame.image.load("player/attack/3attack3.png").convert_alpha()
        elif position == 10:
            player = pygame.image.load("player/attack/3attack4.png").convert_alpha()
        elif position == 11:
            player = pygame.image.load("player/attack/3attack4.png").convert_alpha()
        elif position == 12:
            player = pygame.image.load("player/attack/3attack4.png").convert_alpha()
        elif position == 13:
            player = pygame.image.load("player/attack/3attack5.png").convert_alpha()
        elif position == 14:
            player = pygame.image.load("player/attack/3attack5.png").convert_alpha()
        elif position == 15:
            player = pygame.image.load("player/attack/3attack5.png").convert_alpha()
        elif position == 13:
            player = pygame.image.load("player/attack/3attack6.png").convert_alpha()
        elif position == 14:
            player = pygame.image.load("player/attack/3attack6.png").convert_alpha()
        elif position >= 15:
            player = pygame.image.load("player/attack/3attack6.png").convert_alpha()
            print ("Hello")
            position = 0
            Vera = False
    player = pygame.transform.scale(player, (200, 148)) 
    position +=1   
    return position, player, Vera,Combo

def loading_player_die(position,player,Vera):
    if position == 1:
        player = pygame.image.load("player/die/die0.png").convert_alpha()
    elif position == 2:
        player = pygame.image.load("player/die/die0.png").convert_alpha()
    elif position == 3:
        player = pygame.image.load("player/die/die1.png").convert_alpha()
    elif position == 4:
        player = pygame.image.load("player/die/die1.png").convert_alpha()
    elif position == 5:
        player = pygame.image.load("player/die/die2.png").convert_alpha()
    elif position == 6:
        player = pygame.image.load("player/die/die2.png").convert_alpha()
    elif position == 7:  
        player = pygame.image.load("player/die/die3.png").convert_alpha()           
    elif position == 8:
        player = pygame.image.load("player/die/die3.png").convert_alpha()
    elif position == 9:
        player = pygame.image.load("player/die/die4.png").convert_alpha()
    elif position == 10:
        player = pygame.image.load("player/die/die4.png").convert_alpha()
    elif position == 11:
        player = pygame.image.load("player/die/die5.png").convert_alpha()
    elif position == 12:
        player = pygame.image.load("player/die/die5.png").convert_alpha()
    elif position == 13:
        player = pygame.image.load("player/die/die6.png").convert_alpha()
    elif position == 14:
        player = pygame.image.load("player/die/die6.png").convert_alpha()
        time.sleep(1)
        exit()
        position = 0
        Vera = False
    player = pygame.transform.scale(player, (200, 148)) 
    position +=1   
    return position, player, Vera



def loading_monster_skeleton_walk(mouvement,monster,alive):
        if mouvement == 1:
            monster = pygame.image.load("monsters/skeleton/walk/walk1.png").convert_alpha()
        elif mouvement == 2:
            monster = pygame.image.load("monsters/skeleton/walk/walk1.png").convert_alpha()
        elif mouvement == 3:
            monster = pygame.image.load("monsters/skeleton/walk/walk2.png").convert_alpha()
        elif mouvement == 4:
            monster = pygame.image.load("monsters/skeleton/walk/walk2.png").convert_alpha()
        elif mouvement == 5:
            monster = pygame.image.load("monsters/skeleton/walk/walk3.png").convert_alpha()
        elif mouvement == 6:
            monster = pygame.image.load("monsters/skeleton/walk/walk3.png").convert_alpha()
        elif mouvement == 7:  
            monster = pygame.image.load("monsters/skeleton/walk/walk4.png").convert_alpha()           
        elif mouvement == 8:
            monster = pygame.image.load("monsters/skeleton/walk/walk4.png").convert_alpha()
        elif mouvement == 9:
            monster = pygame.image.load("monsters/skeleton/walk/walk5.png").convert_alpha()
        elif mouvement == 10:
            monster = pygame.image.load("monsters/skeleton/walk/walk5.png").convert_alpha()
        elif mouvement == 11:
            monster = pygame.image.load("monsters/skeleton/walk/walk6.png").convert_alpha()
        elif mouvement == 12:
            monster = pygame.image.load("monsters/skeleton/walk/walk6.png").convert_alpha()
        elif mouvement == 13:
            monster = pygame.image.load("monsters/skeleton/walk/walk7.png").convert_alpha()
        elif mouvement == 14:
            monster = pygame.image.load("monsters/skeleton/walk/walk7.png").convert_alpha()
        elif mouvement == 15:
            monster = pygame.image.load("monsters/skeleton/walk/walk8.png").convert_alpha()
        elif mouvement == 16:
            monster = pygame.image.load("monsters/skeleton/walk/walk8.png").convert_alpha()
        elif mouvement == 17:
            monster = pygame.image.load("monsters/skeleton/walk/walk9.png").convert_alpha()
        elif mouvement == 18:
            monster = pygame.image.load("monsters/skeleton/walk/walk9.png").convert_alpha()
        elif mouvement == 19:
            monster = pygame.image.load("monsters/skeleton/walk/walk10.png").convert_alpha()
        elif mouvement == 20:
            monster = pygame.image.load("monsters/skeleton/walk/walk10.png").convert_alpha()
        elif mouvement == 21:
            monster = pygame.image.load("monsters/skeleton/walk/walk11.png").convert_alpha()
        elif mouvement == 22:  
            monster = pygame.image.load("monsters/skeleton/walk/walk11.png").convert_alpha()           
        elif mouvement == 23:
            monster = pygame.image.load("monsters/skeleton/walk/walk12.png").convert_alpha()
        elif mouvement == 24:
            monster = pygame.image.load("monsters/skeleton/walk/walk12.png").convert_alpha()
        elif mouvement == 25:
            monster = pygame.image.load("monsters/skeleton/walk/walk13.png").convert_alpha()
        elif mouvement >= 26:
            monster = pygame.image.load("monsters/skeleton/walk/walk13.png").convert_alpha()
            mouvement = 0    
        monster = pygame.transform.scale(monster, (120, 123))        
        mouvement +=1   
        return mouvement,monster


def loading_skeleton_death(mouvement,monster,Vera):
    print ("Le mouvement est n*",mouvement)
    if mouvement >= 16:
        mouvement = 0
    if mouvement == 1:
        monster = pygame.image.load("monsters/skeleton/death/death0.png").convert_alpha()
    elif mouvement == 2:
        monster = pygame.image.load("monsters/skeleton/death/death1.png").convert_alpha()
    elif mouvement == 3:
        monster = pygame.image.load("monsters/skeleton/death/death2.png").convert_alpha()
    elif mouvement == 4:
        monster = pygame.image.load("monsters/skeleton/death/death3.png").convert_alpha()
    elif mouvement == 5:
        monster = pygame.image.load("monsters/skeleton/death/death4.png").convert_alpha()
    elif mouvement == 6:
        monster = pygame.image.load("monsters/skeleton/death/death5.png").convert_alpha()
    elif mouvement == 7:  
        monster = pygame.image.load("monsters/skeleton/death/death6.png").convert_alpha()           
    elif mouvement == 8:
        monster = pygame.image.load("monsters/skeleton/death/death7.png").convert_alpha()
    elif mouvement == 9:
        monster = pygame.image.load("monsters/skeleton/death/death8.png").convert_alpha()
        print ("ZABUZA")
    elif mouvement == 10:
        monster = pygame.image.load("monsters/skeleton/death/death9.png").convert_alpha()
    elif mouvement == 11:
        monster = pygame.image.load("monsters/skeleton/death/death10.png").convert_alpha()
    elif mouvement == 12:
        monster = pygame.image.load("monsters/skeleton/death/death11.png").convert_alpha()
    elif mouvement == 13:
        monster = pygame.image.load("monsters/skeleton/death/death12.png").convert_alpha()
    elif mouvement == 14:
        monster = pygame.image.load("monsters/skeleton/death/death13.png").convert_alpha()
    elif mouvement >= 15:
        monster = pygame.image.load("monsters/skeleton/death/death14.png").convert_alpha()
        mouvement = 0
        Vera = False
    monster = pygame.transform.scale(monster, (120, 123))   
    mouvement +=1   
    return mouvement, monster, Vera


def skeleton_AI(mouvement,monster,a,b,c,d,e,player,Vera,player_hitbox_rect,monster_hitbox_rect,animation,alive):
        if animation == 0 and alive == 1 :
            mouvement,monster = loading_monster_skeleton_walk(mouvement,monster,alive)
        elif animation == 1:
            while Vera == True:
                mouvement, monster, Vera = loading_skeleton_death(mouvement,monster,Vera)          
                a,b,c,d,e = update_location(a,b,c,d,e,1)
                monster_hitbox_rect,player_hitbox_rect = affichage(player,background1, background2, background3, background4, background5,paint,road,a,b,c,d,e,monster)
                check_input_exit()
        return mouvement,monster,alive

def loading_player_jump(position,player,Vera):
         
    player = pygame.image.load("player/jump/jump"+str(position)+".png").convert_alpha()

    if position >= 14:
        position = 0
        Vera = False
    player = pygame.transform.scale(player, (200, 148)) 
    position +=1   
    return position, player, Vera

def loading_player_fall(position,player,Vera):
    if position == 1:
        player = pygame.image.load("player/fall/fall0.png").convert_alpha()
    elif position == 2:
        player = pygame.image.load("player/fall/fall0.png").convert_alpha()
    elif position == 3:
        player = pygame.image.load("player/fall/fall0.png").convert_alpha()
    elif position == 4:
        player = pygame.image.load("player/fall/fall1.png").convert_alpha()
    elif position == 5:
        player = pygame.image.load("player/fall/fall1.png").convert_alpha()
    elif position >= 6:  
        player = pygame.image.load("player/fall/fall1.png").convert_alpha()           
        position = 0
        Vera = False
    player = pygame.transform.scale(player, (200, 148)) 
    position +=1   
    return position, player, Vera


def dash(position,a,b,c,d,e,player,Vera,Combo,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive):
        position = 1
        while Vera == True:
            clock.tick(20)
            position, player, Vera, Combo = loading_player_attack(position,player,Vera,Combo)
            mouvement,monster,alive = skeleton_AI(mouvement,monster,a,b,c,d,e,player,False,player_hitbox_rect,monster_hitbox_rect,0,alive)
            a,b,c,d,e = update_location(a,b,c,d,e,1)
            monster_hitbox_rect,player_hitbox_rect = affichage(player,background1, background2, background3, background4, background5,paint,road,a,b,c,d,e,monster)
            collide_hit,alive = collide(player_hitbox_rect, monster_hitbox_rect,1,position,a,b,c,d,e,player,0,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive)
            print ("Collide_hit = ",collide_hit)
            if collide_hit == 1 :
                mouvement,monster,alive = skeleton_AI(mouvement,monster,a,b,c,d,e,player,True,player_hitbox_rect,monster_hitbox_rect,1,alive)
            check_input_exit()
        return position,a,b,c,d,e,mouvement,monster,alive

def die(position,a,b,c,d,e,player,Vera,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive):
        position = 1
        while Vera == True:
            clock.tick(20)
            position, player, Vera = loading_player_die(position,player,Vera)
            mouvement,monster,alive = skeleton_AI(mouvement,monster,a,b,c,d,e,player,False,player_hitbox_rect,monster_hitbox_rect,0,alive)
            a,b,c,d,e = update_location(a,b,c,d,e,1)
            monster_hitbox_rect,player_hitbox_rect = affichage(player,background1, background2, background3, background4, background5,paint,road,a,b,c,d,e,monster)
            check_input_exit()
        return position,a,b,c,d,e,mouvement
def jump(position,a,b,c,d,e,player,Vera,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive):
        position = 1
        while Vera == True:
            clock.tick(20)
            position, player, Vera = loading_player_jump(position,player,Vera)
            monster_hitbox_rect,player_hitbox_rect = affichage(player,background1, background2, background3, background4, background5,paint,road,a,b,c,d,e,monster)
            mouvement,monster,alive = skeleton_AI(mouvement,monster,a,b,c,d,e,player,False,player_hitbox_rect,monster_hitbox_rect,0,alive)
            a,b,c,d,e = update_location(a,b,c,d,e,1)
            
            if position > 3:
                d = d * 0.85
            check_input_exit()
        d += +40
        while d != 432:
            clock.tick(20)
            position, player, Vera = loading_player_fall(position,player,Vera)
            mouvement,monster,alive = skeleton_AI(mouvement,monster,a,b,c,d,e,player,False,player_hitbox_rect,monster_hitbox_rect,0,alive)
            a,b,c,d,e = update_location(a,b,c,d,e,1)
            monster_hitbox_rect,player_hitbox_rect = affichage(player,background1, background2, background3, background4, background5,paint,road,a,b,c,d,e,monster)
            d = d * 1.15
            if d >= 432:
                d = 432
        return position,a,b,c,d,e,mouvement





def affichage(player,background1, background2, background3, background4, background5,paint,road,a,b,c,d,e,monster):
    win.blit(background1, (0 ,0), (a,0,432,768))
    win.blit(background3, (70 ,330), (0,0,432,768))
    win.blit(background2, (0 ,230), (a,0,432,768))
    win.blit(background4, (0 ,-130), (a,0,432,768))
    win.blit(background5, (0 ,400), (a,0,432,768))
    monster_hitbox_rect, player_hitbox_rect = load_rect(c,d,e)
    win.blit(monster, (e,455))
    

    win.blit(paint, (0,600))
    # win.blit(road, (0,352),   (b,0,432,200))
    win.blit(player, (c,d))
    pygame.display.flip()
    return monster_hitbox_rect,player_hitbox_rect

def update_location(a,b,c,d,e,max):
        
    a +=  1

    b +=  2

    e += -3

    if max == 1:
        a +=  -1
        b +=  -1
        e += -1.5
    if a >= 1920:
        a = 0
    if b >= 900:
        b = 0
    return a,b,c,d,e

def collide (rect1, rect2,attack,position,a,b,c,d,e,player,Vera,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive):
    collide_hit = 0
    if rect1.colliderect(rect2):
        if attack == 0 and alive == 1:
            die(position,a,b,c,d,e,player,1,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive)
        if attack == 1 and alive == 1:
            collide_hit = 1
            alive = 0
            # monster_hitbox_rect = pygame.draw.rect(win, (0, 200, 0), (e+10,  1000, 50, 130))
            # player_hitbox_rect = pygame.draw.rect(win, (200, 0, 0), (c+90,  1000, 50, 130))
    return collide_hit, alive



def load_rect(c,d,e):
    monster_hitbox_rect = pygame.draw.rect(win, (0, 200, 0), (e+10,  455, 50, 130))
    player_hitbox_rect = pygame.draw.rect(win, (200, 0, 0), (c+90,  d+23, 50, 130))
    return monster_hitbox_rect,player_hitbox_rect

def sound_menu_theme(x):
    if x == 0:
        pygame.mixer.music.load("son.mp3")
        volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()
    if x == 1:
        volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0)
    if x == 2:
        volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0.05)


if __name__ == "__main__":

    pygame.init()
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((432, 768))
    sound_menu_theme(0)
    position = 1
    mouvement = 1
    background1, background2, background3, background4, background5 , paint , road,monster = loading_picture()
    a = 0
    b = 0
    c = -40
    d = 432
    e = 400
    Combo = 0
    monster_hitbox_rect,player_hitbox_rect = load_rect(c,d,e)
    alive = 1

    spell1_rect = pygame.draw.rect(win, (0, 200, 0), (62,  637, 62, 89))

    # background = pygame.image.load("background.png").convert()
    while True:
        clock.tick(20)
        position, player = loading_player_sprite(position,0)
        mouvement,monster,alive = skeleton_AI(mouvement,monster,a,b,c,d,e,player,False,player_hitbox_rect,monster_hitbox_rect,0,alive)
        monster_hitbox_rect,player_hitbox_rect = affichage(player,background1, background2, background3, background4, background5,paint,road,a,b,c,d,e,monster)
        a,b,c,d,e = update_location(a,b,c,d,e,0)
        collide_hit, alive = collide(player_hitbox_rect, monster_hitbox_rect,0,position,a,b,c,d,e,player,1,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive)
        check_input_exit()
        mouse_pos = pygame.mouse.get_pos()
        mouse_p = pygame.mouse.get_pressed()
        if mouse_p[0] == True :
            if spell1_rect.collidepoint(mouse_pos):
                Combo +=1
                if Combo > 3:
                    Combo = 1
                position,a,b,c,d,e,mouvement,monster,alive = dash(position,a,b,c,d,e,player,True,Combo,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive)
        if mouse_p[1] == True :  #bouton molette
            position,a,b,c,d,e,mouvement = jump(position,a,b,c,d,e,player,True,mouvement,monster,player_hitbox_rect,monster_hitbox_rect,alive)
        if mouse_p[2] == True :
            print("Hello")
        
        # if event.type == pygame.KEYDOWN:                                                         
        #     if event.key == pygame.K_UP:
        #         print ("Hi")
        
        pygame.display.flip()
        