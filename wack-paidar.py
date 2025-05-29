import pygame # klíčová knihovna umožňující vytvářet jednoduše nejen hry
import random
import time
pygame.init() # nutný příkaz hned na začátku pro správnou inicializaci knihovny
bg_music = pygame.mixer.Sound("music.mp3")

window_width = 800
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
    # dvojice (w,h) v parametru se nazývá *tuple*
pygame.display.set_caption("Zmlať Paidara") # nastavíme do hlavičky okna název hry
# Load and set the window icon
#icon = pygame.image.load("paidar.png")  # Make sure the image is in the same directory
#pygame.display.set_icon(icon)

clock = pygame.time.Clock()

sky_surface = pygame.Surface((window_width,0.55*window_height))
sky_surface.fill("darkslategray1")
ground_surface = pygame.Surface((window_width,0.45*window_height))
ground_surface.fill("lightsalmon4")

# text
text_font = pygame.font.Font("PixelifySans.ttf",100)
text_surface = text_font.render("GAME OVER!", True, "Black")
text_rect = text_surface.get_rect(center=(window_width/2, window_height/2))

# class Tung_sahur_basebalka(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__() # volá konstruktor třídy Sprite, od které dědíme
#         bat_1 = pygame.image.load("man_1.png")
#         bat_2 = pygame.image.load("man_2.png")
#         bat_3 = pygame.image.load("man_3.png")
#         bat_4 = pygame.image.load("man_4.png")
#         self.hit_images_images = [bat_1,bat_2,bat_3,bat_4]
#         self.walking_index = 0
#         self.image = self.hit_images[self.walking_index]
game_active = True
counter = 0
while True:
    # zjistíme co dělá hráč za akci
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # zavřeme herní okno
            exit() # úplně opustíme herní smyčku, celý program se ukončí
        if event.type == pygame.KEYDOWN:
            if game_active == False:
                game_active=True
                bg_music.play()

    if game_active:
        # pozadí
        screen.blit(sky_surface,(0,0)) # položíme sky_surface na souřadnice [0,0]
        screen.blit(ground_surface,(0,0.55*window_height)) # položíme ground_surface na souřadnice [0,300] (pod oblohu)

        if counter > 120:
            counter = 0
           
        else:
            counter += 1
