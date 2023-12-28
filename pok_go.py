import pygame
import sys
import random
import time
import os
import math
from pygame.locals import*

def resource_path(relative_path):
    return "Assets/"+relative_path

all_resources = {
    "front_right" : resource_path("front_right.png"),
    "front_left" : resource_path("front_left.png"),
    "front_stand" : resource_path("front_standing.png"),
    "back_right" : resource_path("back_right.png"),
    "back_left" : resource_path("back_left.png"),
    "back_stand" : resource_path("back_stand.png"),
    "left_walk" : resource_path("left_Lwalk.png"),
    "left_stand" : resource_path("left_stand.png"),
    "right_walk" : resource_path("right_Lwalk.png"),
    "right_stand" : resource_path("stand_right.png"),
    "background" : resource_path("6.png"),
    "bulbasour" : resource_path("bulbasour.png"),
    "squirtle" : resource_path("squirtel.png"),
    "charmander" : resource_path("charmander.png"),
    "pikachu" : resource_path("pikachu.png"),
    "trainer2" : resource_path("trainer4.png"),
    "trainer1" : resource_path("trainer2.png"),
    "sleep_z" : resource_path("zzz.png")
}

pygame.init()
screenheight = 640
screenwidth = 384
screen = pygame.display.set_mode((screenwidth,screenheight))
CLOCK = pygame.time.Clock()
FPS = 64
pygame.display.set_caption('Pokemon Go!')
FPSClock = pygame.time.Clock()
character_size = (30,40)
list_index = 1
image_index = 0
comp1_XP = 114
comp2_XP = 114
player1_XP = 114
player2_XP = 114
if comp1_XP > 0 and comp2_XP > 0:
    rnd = random.randint(0,1)
else:
    rnd = 0
turn = 0
contact_time = 0

front_right = pygame.transform.scale(pygame.image.load(all_resources["front_right"]).convert_alpha(),character_size)
front_left = pygame.transform.scale(pygame.image.load(all_resources["front_left"]).convert_alpha(),character_size)
front_stand = pygame.transform.scale(pygame.image.load(all_resources["front_stand"]).convert_alpha(),character_size)

back_right = pygame.transform.scale(pygame.image.load(all_resources["back_right"]).convert_alpha(),character_size)
back_left = pygame.transform.scale(pygame.image.load(all_resources["back_left"]).convert_alpha(),character_size)
back_stand = pygame.transform.scale(pygame.image.load(all_resources["back_stand"]).convert_alpha(),character_size)

left_walk = pygame.transform.scale(pygame.image.load(all_resources["left_walk"]).convert_alpha(),character_size)
left_stand = pygame.transform.scale(pygame.image.load(all_resources["left_stand"]).convert_alpha(),character_size)

right_walk = pygame.transform.scale(pygame.image.load(all_resources["right_walk"]).convert_alpha(),character_size)
right_stand = pygame.transform.scale(pygame.image.load(all_resources["right_stand"]).convert_alpha(),character_size)

pikachu = pygame.transform.scale(pygame.image.load(all_resources["pikachu"]).convert_alpha(),character_size)
pikachu_rect = pikachu.get_rect(center = (310,70))
charmander = pygame.transform.scale(pygame.image.load(all_resources["charmander"]).convert_alpha(),character_size)
charmander_rect = charmander.get_rect(center = (250,255))
bulbasaur = pygame.transform.scale(pygame.image.load(all_resources["bulbasour"]).convert_alpha(),character_size)
bulbasaur = pygame.transform.flip(bulbasaur,True,False)
bulbasaur_rect = charmander.get_rect(center = (50,130))
squirtle = pygame.transform.scale(pygame.image.load(all_resources["squirtle"]).convert_alpha(),character_size)
squirtle = pygame.transform.flip(squirtle,True,False)
squirtle_rect = charmander.get_rect(center = (40,430))

trainer1 = pygame.transform.scale(pygame.image.load(all_resources["trainer1"]).convert_alpha(),(25,40))
trainer2 = pygame.transform.scale(pygame.image.load(all_resources["trainer2"]).convert_alpha(),(25,40))
sleep_z = pygame.transform.scale(pygame.image.load(all_resources["sleep_z"]).convert_alpha(),(45,33))

player_list = [
    [front_stand,front_left,front_right],
    [back_stand,back_left,back_right],
    [left_stand,left_walk],
    [right_stand,right_walk]
]

trainer_x = {0 : 180, 1 : 320, 2 : 320, 3 : 130, 4 : 100, 5 : 120, 6 : 60, 7 : 70, 8 : 150, 9 : 180, 10 : 240, 11 : 170, 12 : 290, 13 : 190, 14 : 230}
trainer_y = {0 : 440, 1 : 410, 2 : 340, 3 : 330, 4 : 290, 5 : 310, 6 : 230, 7 : 180, 8 : 210, 9 : 240, 10 : 190, 11 : 270, 12 : 220, 13 : 90, 14 : 430}
trainer1_index = random.randint(0,14)
trainer2_index = random.randint(0,14)
if trainer2_index == trainer1_index:
    trainer2_index = random.randint(0,14)
trainer1_rect = trainer1.get_rect(center = (trainer_x[trainer1_index], trainer_y[trainer1_index]))
trainer2_rect = trainer2.get_rect(center = (trainer_x[trainer2_index], trainer_y[trainer2_index]))
t1_x = trainer1_rect.x
t1_y = trainer1_rect.y
t2_x = trainer2_rect.x
t2_y = trainer2_rect.y

poki_info = {"pikachu" : {"pos" : (310,70), "rect" : pikachu_rect, "image" : pikachu, "name" : "pikachu"}, 
"bulbasaur" : {"pos" : (310,70), "rect" : bulbasaur_rect, "image" : bulbasaur, "name" : "bulbasaur"},
"charmander" : {"pos" : (310,70), "rect" : charmander_rect, "image" : charmander, "name" : "charmander"},
"squirtle" : {"pos" : (310,70), "rect" : squirtle_rect, "image" : squirtle, "name" : "squirtle"} }

attackData = {
    "pikachu":{"name" : ["Thunderbolt","Tackel"],"attack_level" : [30,40]},
    "bulbasaur":{"name" : ["Razor Leaf","Poison Seed"],"attack_level" :[23,60]},
    "charmander":{"name" : ["Fire Ball","Fire Tornado"],"attack_level" :[30,35]},
    "squirtle":{"name" : ["Water Splash","Tackel"],"attack_level" :[20,10]}
}

x = 185
y = 600
speed = 10
click = 0
turn = 0

left_collide = False
right_collide = False
down_collide = False
up_collide = False
inContact = False
denied = False
accepted = False
clicked =  False
choosen1 = False
game_over = False
tired = False

player_rect = back_stand.get_rect(center = (x,y))

bg = pygame.image.load(all_resources["background"]).convert_alpha()
screen.blit(bg,(0,0))
no = 0

SCREENTIMER = pygame.USEREVENT + 1
pygame.time.set_timer(SCREENTIMER,1000) 

def player_animation():
    newPlayer = player_list[list_index][image_index]
    global new_rect
    new_rect = newPlayer.get_rect(center = (player_rect.centerx,player_rect.centery))
    return newPlayer,new_rect

def left_border_control():
    if player_rect.x < 30: 
        return True
    if player_rect.x < 160:
        if player_rect.y <= 600 and player_rect.y >= 530:
            return True
    if player_rect.x < 115:
        if player_rect.y <= 510 and player_rect.y >= 460:
            return True
    if player_rect.x < 235:
        if player_rect.y <= 400 and player_rect.y >= 340:
            return True
    
    return False

def right_border_control():
    if player_rect.x > 320:
        return True
    if player_rect.x > 250:
        if player_rect.y <= 190 and player_rect.y >= 140:
            return True
    if player_rect.x > 170:
        if player_rect.y <= 600 and player_rect.y >= 540:
            return True

    if player_rect.x >= 245:
        if player_rect.y <= 510 and player_rect.y >= 450:
            return True

    return False

def down_border_control():
    if player_rect.y >= 440:
        if player_rect.x <= 85 and player_rect.x >= 25:
            return True
        if player_rect.x <= 315 and player_rect.x >= 255:
            return True
    if player_rect.y == 330:
        if player_rect.x <= 215 and player_rect.x >= 25:
            return True
    if player_rect.y >= 600:
        return True
    if player_rect.y > 505:
        if player_rect.x <= 135 and player_rect.x >= 105:
            return True
    if player_rect.y >= 505:
        if player_rect.x <= 235 and player_rect.x >= 195:
            return True
    if player_rect.y == 120:
        if player_rect.x <= 325 and player_rect.x >= 275:
            return True
            
    return False

def up_border_control():
    if player_rect.y < 60:
        return True
    if player_rect.y == 410:
        if player_rect.x <= 215 and player_rect.x >= 25:
            return True
    if player_rect.y == 190:
        if player_rect.x <= 325 and player_rect.x >= 270:
            return True

    return False

def sprites():
    screen.blit(bg,(0,0))
    screen.blit(charmander,charmander_rect)
    screen.blit(pikachu,pikachu_rect)
    screen.blit(squirtle,squirtle_rect)
    screen.blit(bulbasaur,bulbasaur_rect)
    screen.blit(trainer1,trainer1_rect)
    screen.blit(trainer2,trainer2_rect)

def in_contact():
    dist1 = abs(math.sqrt((player_rect.x - t1_x) **2 + (player_rect.y - t1_y)**2))
    dist2 = abs(math.sqrt((player_rect.x - t2_x) **2 + (player_rect.y - t2_y)**2))
    inContact_t1 = 0
    inContact_t2 = 0
    if dist1 <= 40:
        inContact_t1 = 1
        if inContact_t2 <= 0:
            if no <= 0:
                return True
            else:
                return False
        elif inContact_t2 >= 1:
            if no >= 1:
                return True
            else:
                return False
    elif dist2 <= 40:
        inContact_t2 = 1
        if inContact_t1 <= 0:
            if no <= 0:
                return True
            else:
                return False
        elif inContact_t1 >= 1:
            if no >= 1:
                return True
            else:
                return False

    else:
        return False
    
def draw_rect():
    pygame.draw.rect(screen, (220,220,220), pygame.Rect(8, screenheight - 140, screenwidth - 15, 135))
    pygame.draw.rect(screen, (210,210,210), pygame.Rect(15, screenheight - 132, screenwidth - 27, 120))

def draw_rectt():
    pygame.draw.rect(screen, (230,230,230), pygame.Rect(8, screenheight - 140, screenwidth - 15, 135))
    
def write_text(text,ani,colour,coords,size,bold=False):
    font = pygame.font.SysFont('monospace',size,bold = bold)
    txt = font.render(text,ani,colour)
    txt_rect = txt.get_rect(midleft = coords)
    screen.blit(txt,txt_rect)
    return txt,txt_rect

def write_txt(text,ani,colour,coords,size,bold=False):
    font = pygame.font.SysFont('monospace',size,bold = bold)
    txt = font.render(text,ani,colour)
    txt_rect = txt.get_rect(center = coords)
    screen.blit(txt,txt_rect)
    return txt,txt_rect

def attack(name):
    global attack1_text,attack1_rect,attack2_text,attack2_rect,pok_img,player_text,playerText_rect,clicked
    if name == "pikachu":
        attack1_text,attack1_rect = write_txt(attackData["pikachu"]["name"][0],True,(50,50,50),(95,575),20,bold = False) 
        attack2_text,attack2_rect = write_txt(attackData["pikachu"]["name"][1],True,(50,50,50),(270,575),20,bold = False)
        player_text,playerText_rect = write_text(poki_info["pikachu"]["name"],True,(50,50,50),(28,360),18,bold = True)
        pok_img = poki_info["pikachu"]["image"]
        clicked = True
    elif name == "bulbasaur":
        attack1_text,attack1_rect = write_txt(attackData["bulbasaur"]["name"][0],True,(50,50,50),(95,575),20,bold = False) 
        attack2_text,attack2_rect = write_txt(attackData["bulbasaur"]["name"][1],True,(50,50,50),(270,575),20,bold = False)
        player_text,playerText_rect = write_text(poki_info["bulbasaur"]["name"],True,(50,50,50),(28,360),18,bold = True)
        pok_img = poki_info["bulbasaur"]["image"]
        clicked = True
    elif name == "charmander": 
        attack1_text,attack1_rect = write_txt(attackData["charmander"]["name"][0],True,(50,50,50),(95,575),20,bold = False) 
        attack2_text,attack2_rect = write_txt(attackData["charmander"]["name"][1],True,(50,50,50),(270,575),20,bold = False)
        player_text,playerText_rect = write_text(poki_info["charmander"]["name"],True,(50,50,50),(28,360),18,bold = True)
        pok_img = poki_info["charmander"]["image"]
        clicked = True
    elif name == "squirtle":
        attack1_text,attack1_rect = write_txt(attackData["squirtle"]["name"][0],True,(50,50,50),(95,575),20,bold = False) 
        attack2_text,attack2_rect = write_txt(attackData["squirtle"]["name"][1],True,(50,50,50),(270,575),20,bold = False)
        player_text,playerText_rect = write_text(poki_info["squirtle"]["name"],True,(50,50,50),(28,360),18,bold = True)
        pok_img = poki_info["squirtle"]["image"]
        clicked = True
    screen.blit(pok_img,(40,420))

def game_accepted():
    screen.fill((250,250,250))
    draw_rectt()
    screen.blit(poki_info[comp_card[rnd]]["image"],(250,110))
    pygame.draw.rect(screen, (220,220,220), pygame.Rect(240, 80, 114, 23))

    if rnd == 0 and len(comp_card) > 1:
        pygame.draw.rect(screen, (0,250,0), pygame.Rect(240, 80,comp1_XP, 23))
    elif rnd == 1 and len(comp_card) > 1:
        pygame.draw.rect(screen, (0,250,0), pygame.Rect(240, 80,comp2_XP, 23))
    else:
        if rnd == 0:
            if comp1_XP > 0:
                pygame.draw.rect(screen, (0,250,0), pygame.Rect(240, 80,comp1_XP, 23))
            elif comp2_XP > 0:
                pygame.draw.rect(screen, (0,250,0), pygame.Rect(240, 80,comp2_XP, 23))

    XP1,XP1_rect = write_text("XP",True,(50,50,50),(28,380),14,bold = False)
    XP2,XP2_rect = write_text("XP",True,(50,50,50),(240,70),14,bold = False)

    comp_text,compText_rect = write_text(poki_info[comp_card[rnd]]["name"],True,(50,50,50),(240,50),18,bold = True)
    pygame.draw.rect(screen, (220,220,220), pygame.Rect(25, 390, 114, 23))
    
def gen_pok():
    pok_index = random.randint(0,3)
    pok_list = ["pikachu","bulbasaur","charmander","squirtle"]
    return pok_list[pok_index]

battle = {
    "comp":{"data":[gen_pok() for i in range(2)]},
    "user":{"data":[gen_pok() for i in range(2)]}
}

comp_card = battle["comp"]["data"]
if comp_card[0] == comp_card[1]:
    comp_card[0] = gen_pok()
player_card = battle["user"]["data"]
if player_card[0] == player_card[1]:
    player_card[0] = gen_pok()
att_rnd = random.randint(0,1)
random_handler= (0,0)
comp_pok1 = comp_card[0]
comp_pok2 = comp_card[1]

def check_handled(pygame):
    """
    This function takes the current pygame object
    will see what's the position of mouse down if it's same as before we have already habdled the situation
    """
    global random_handler
    current = pygame.mouse.get_pos()
    result = current[0] == random_handler[0] and current[1] == random_handler[1]
    random_handler = current
    return result

        

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if inContact == False and denied == False:
                if event.key == K_DOWN:
                    if list_index == 1 or list_index == 2 or list_index == 3:
                        image_index = 4
                    list_index = 0
                    if down_collide == False:
                        player_rect.centery += speed
                    image_index += 1
                    if image_index == 3:
                        image_index = 1
                    if image_index > 3:
                        image_index = 0
           
                if event.key == K_UP:
                    front = False
                    if list_index == 0 or list_index == 2 or list_index == 3:
                        image_index = 4
                    list_index = 1
                    if up_collide == False:
                        player_rect.centery -= speed
                    image_index += 1
                    if image_index == 3:
                        image_index = 1
                    if image_index > 3:
                        image_index = 0

                if event.key == K_LEFT:
                    if list_index == 0 or list_index == 1 or list_index == 3:
                        image_index = 2
                    list_index = 2
                    image_index += 1
                    if left_collide == False:
                        player_rect.centerx -= speed
                    if image_index > 1:
                        image_index = 0

                if event.key == K_RIGHT:
                    if list_index == 0 or list_index == 1 or list_index == 2:
                        image_index = 2
                    list_index = 3
                    image_index += 1
                    if right_collide == False:
                        player_rect.centerx += speed
                    if image_index > 1:
                        image_index = 0
        
        if event.type == SCREENTIMER:
            if inContact or denied or tired or game_over:
                if contact_time < 2:
                    contact_time += 1

        
    left_collide = left_border_control()
    right_collide = right_border_control()
    down_collide = down_border_control()
    up_collide = up_border_control()
    
    sprites()
    player_list[list_index][image_index],player_rect = player_animation()
    screen.blit(player_list[list_index][image_index],player_rect)
    inContact = in_contact()
    if inContact:
        draw_rect()
        
        if denied == False and accepted == False:
            first_text,first_rect = write_txt("Trainer wants to fight",True,(50,50,50),(190,545),20,bold = True)
            first_text,first_rect = write_txt("with you!",True,(50,50,50),(190,570),20,bold = True)
            display_time = pygame.time.get_ticks()
            
            if contact_time >= 2:
                draw_rect()
                sec_text,sec_rect = write_txt("Are you ready?",True,(50,50,50),(190,540),20,bold = True)
                yes_text,yes_rect = write_text("Yes",True,(50,50,50),(100,585),20,bold = False)
                no_text,no_rect = write_text("No",True,(50,50,50),(235,585),20,bold = False)
                if event.type == pygame.MOUSEMOTION: 
                    if pygame.mouse.get_pos() and yes_rect.collidepoint(pygame.mouse.get_pos()): 
                        yes_text,yes_rect = write_text("Yes",True,(50,50,50),(100,585),20,bold = True)
                    if pygame.mouse.get_pos() and no_rect.collidepoint(pygame.mouse.get_pos()): 
                        no_text,no_rect = write_text("No",True,(50,50,50),(235,585),20,bold = True)
        if event.type == pygame.MOUSEBUTTONDOWN and not check_handled(pygame):
            if pygame.mouse.get_pressed()[0] and no_rect.collidepoint(pygame.mouse.get_pos()):
                no += 1
                denied = True
                contact_time = 0
            
            if pygame.mouse.get_pressed()[0] and yes_rect.collidepoint(pygame.mouse.get_pos()):
                no += 1
                accepted = True
                turn += 1
                contact_time = 0

    if denied:
        draw_rect()
        denied_text,denied_rect = write_txt("You denied the challenge",True,(50,50,50),(190,555),20,bold = True)
        if contact_time >= 2:
            denied = False
            contact_time = 0

    if accepted:
        if turn == 2:
            comp_card.clear()
            comp1_XP = 114
            comp2_XP = 114
            player1_XP = 114
            player2_XP = 114
            comp_card.append(comp_pok1)
            comp_card.append(comp_pok2)
            turn += 1
        
        if comp1_XP <= 0 and len(comp_card) > 1:
            comp_card.remove(comp_pok1)
        if comp2_XP <= 0 and len(comp_card) > 1:
            comp_card.remove(comp_pok2)
        
    
        game_accepted()
        if tired:
            draw_rectt()
            tired_text,tired_rect = write_txt(poki_info[player_card[0]]["name"]+" went to sleep",True,(50,50,50),(188,555),20,bold = True)
            screen.blit(poki_info[player_card[click]]["image"],(40,420))
            pok_text,pok_rect = write_text(poki_info[player_card[click]]["name"],True,(50,50,50),(28,360),18,bold = True)
            clicked = False
            if contact_time >= 2:
                contact_time = 0
                tired = False
            

        if clicked and not tired:
            draw_rectt()
            if click == 0:
                player_index = player_card[0]
                pygame.draw.rect(screen, (0,250,0), pygame.Rect(25, 390,player1_XP, 23))
            elif click == 1:
                player_index = player_card[1]
                pygame.draw.rect(screen, (0,250,0), pygame.Rect(25, 390,player2_XP, 23))
            attack(poki_info[player_index]["name"])
            choose_text,choose_rect = write_txt("Choose Attack",True,(50,50,50),(190,530),20,bold = True)

            if event.type == pygame.MOUSEMOTION: 
                attack(poki_info[player_index]["name"])
                if pygame.mouse.get_pos() and attack1_rect.collidepoint(pygame.mouse.get_pos()): 
                    attack1_text,attack1_rect = write_txt(attackData[player_index]["name"][0],True,(50,50,50),(95,575),20,bold = True) 
                elif pygame.mouse.get_pos() and attack2_rect.collidepoint(pygame.mouse.get_pos()): 
                    attack2_text,attack2_rect = write_txt(attackData[player_index]["name"][1],True,(50,50,50),(270,575),20,bold = True)

            if event.type == pygame.MOUSEBUTTONDOWN and not check_handled(pygame):
                attack(poki_info[player_index]["name"])
                if pygame.mouse.get_pressed()[0] and attack1_rect.collidepoint(pygame.mouse.get_pos()):
                    if attackData[player_index]["attack_level"][0] < attackData[comp_card[rnd]]["attack_level"][att_rnd]:
                        if choosen1 == True:
                            player1_XP -= attackData[comp_card[rnd]]["attack_level"][att_rnd]
                        else:
                            player2_XP -= attackData[comp_card[rnd]]["attack_level"][att_rnd]
                    else:
                        if rnd == 0 and comp1_XP > 0 or comp2_XP > 0:
                            comp1_XP -= attackData[player_index]["attack_level"][0]
                        elif rnd == 1 and comp1_XP > 0 or comp2_XP > 0:
                            comp2_XP -= attackData[player_index]["attack_level"][0]
                        else:
                            if comp1_XP > 0:
                                comp1_XP -= attackData[player_index]["attack_level"][0]
                            elif comp2_XP > 0:
                                comp2_XP -= attackData[player_index]["attack_level"][0]
                        
                    clicked = False
                    choosen1 = False
                    if comp1_XP > 0 and comp2_XP > 0:
                        rnd = random.randint(0,1)
                    else:
                        rnd = 0
                    att_rnd = random.randint(0,1)
                    
                if pygame.mouse.get_pressed()[0] and attack2_rect.collidepoint(pygame.mouse.get_pos()):
                    if attackData[player_index]["attack_level"][1] < attackData[comp_card[rnd]]["attack_level"][att_rnd]:
                        if choosen1 == True:
                            player1_XP -= attackData[comp_card[rnd]]["attack_level"][att_rnd]
                        else:
                            player2_XP -= attackData[comp_card[rnd]]["attack_level"][att_rnd]
                    else:
                        if rnd == 0:
                            comp1_XP -= attackData[player_index]["attack_level"][0]
                            rnd = 0
                        elif rnd == 1:
                            comp2_XP -= attackData[player_index]["attack_level"][0]
                            rnd = 0
                    clicked = False  
                    choosen1 = False 
                    if comp1_XP > 0 and comp2_XP > 0:  
                        rnd = random.randint(0,1)
                    else:
                        rnd = 0
                    att_rnd = random.randint(0,1)
           
        if clicked == False and not tired:
            draw_rectt()
            pok_text1,pok1_rect = write_txt(poki_info[player_card[0]]["name"],True,(50,50,50),(95,575),20,bold = False) 
            pok_text2,pok2_rect = write_txt(poki_info[player_card[1]]["name"],True,(50,50,50),(270,575),20,bold = False)
            choose_text,choose_rect = write_txt("Choose Pokemon",True,(50,50,50),(190,530),20,bold = True)

            if event.type == pygame.MOUSEMOTION: 
                if pygame.mouse.get_pos() and pok1_rect.collidepoint(pygame.mouse.get_pos()): 
                    pok_text1,pok1_rect = write_txt(poki_info[player_card[0]]["name"],True,(50,50,50),(95,575),20,bold = True)
                    player_text,playerText_rect = write_text(poki_info[player_card[0]]["name"],True,(50,50,50),(28,360),18,bold = True)
                    screen.blit(poki_info[player_card[0]]["image"],(40,420))
                    pygame.draw.rect(screen, (0,250,0), pygame.Rect(25, 390,player1_XP, 23))

                elif pygame.mouse.get_pos() and pok2_rect.collidepoint(pygame.mouse.get_pos()): 
                    pok_text2,pok2_rect = write_txt(poki_info[player_card[1]]["name"],True,(50,50,50),(270,575),20,bold = True)
                    player_text,playerText_rect = write_text(poki_info[player_card[1]]["name"],True,(50,50,50),(28,360),18,bold = True)
                    screen.blit(poki_info[player_card[1]]["image"],(40,420))
                    pygame.draw.rect(screen, (0,250,0), pygame.Rect(25, 390,player2_XP, 23))

                else:
                    player_text,playerText_rect = write_text(poki_info[player_card[0]]["name"],True,(50,50,50),(28,360),18,bold = True)
                    screen.blit(poki_info[player_card[0]]["image"],(40,420))
                    pygame.draw.rect(screen, (0,250,0), pygame.Rect(25, 390,player1_XP, 23))

                
            else:
                player_text,playerText_rect = write_text(poki_info[player_card[0]]["name"],True,(50,50,50),(28,360),18,bold = True)
                screen.blit(poki_info[player_card[0]]["image"],(40,420))
                pygame.draw.rect(screen, (0,250,0), pygame.Rect(25, 390,player1_XP, 23))

            if event.type == pygame.MOUSEBUTTONDOWN and not check_handled(pygame):
                if pygame.mouse.get_pressed()[0] and pok1_rect.collidepoint(pygame.mouse.get_pos()):
                    click = 0
                    attack(poki_info[player_card[0]]["name"])
                    if player1_XP <= 0:
                        tired = True
                        choosen1 = False
                    else:
                        clicked = True
                        choosen1 = True                    
                elif pygame.mouse.get_pressed()[0] and pok2_rect.collidepoint(pygame.mouse.get_pos()):
                    click = 1
                    attack(poki_info[player_card[1]]["name"])
                    if player2_XP <= 0:
                        clicked = False
                        tired = True
                    else:
                        clicked = True
                        choosen1 = False

        if (player1_XP + player2_XP) <= 0 or (comp1_XP + comp2_XP) <= 0:
            draw_rectt()
            game_over = True
            accepted = False

    if game_over:
        draw_rect()
        if (player1_XP + player2_XP) <= (comp1_XP + comp2_XP):
            over_text,over_rect = write_txt("You Loose!",True,(50,50,50),(192,550),20,bold = True) 
            over_text1,over1_rect = write_txt("Better Luck Next Time.",True,(50,50,50),(192,570),20,bold = True)
        elif (player1_XP + player2_XP) == (comp1_XP + comp2_XP):
            over_text,over_rect = write_txt("Game Tied. Nice Fight",True,(50,50,50),(192,550),20,bold = True)
        elif (player1_XP + player2_XP) >= (comp1_XP + comp2_XP):
            over_text,over_rect = write_txt("You Win! Amazing Job.",True,(50,50,50),(192,550),20,bold = True)
        if contact_time >= 2:
            contact_time = 0
            game_over = False    

    pygame.display.update()
    FPSClock.tick(FPS)