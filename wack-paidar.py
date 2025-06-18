import pygame # klíčová knihovna umožňující vytvářet jednoduše nejen hry
import random
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init() # nutný příkaz hned na začátku pro správnou inicializaci knihovny
bg_music = pygame.mixer.Sound("Megalovania.mp3")
damage_1 = pygame.mixer.Sound("damage1.mp3")
damage_2 = pygame.mixer.Sound("damage2.mp3")
vyhra = pygame.mixer.Sound("výhra.mp3")
prohra =pygame.mixer.Sound("prohra.mp3")
prohra2 =pygame.mixer.Sound("prohra2.mp3")

# herní okno
window_width = 600
window_height = 600
cell_size = 150
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Zachraň GCHD před Paidlerem")
icon = pygame.image.load("logo.png")  # Make sure the image is in the same directory
pygame.display.set_icon(icon)
background_image = pygame.image.load("gchd.jpg").convert()
background_image = pygame.transform.scale(background_image, (window_width, window_height))
clock = pygame.time.Clock()
text_font = pygame.font.Font("PixelifySans.ttf",50)
grid = [(x, y) for x in range(0, window_width, cell_size) for y in range(0, window_height, cell_size)]
object_size = 120
object_offset = (cell_size - object_size) // 2

class Mole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("paidar_tank.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (object_size, object_size))
        self.rect = self.image.get_rect()
        self.new_position()

    def new_position(self):
        pozice = random.choice(grid)
        self.rect.topleft = (pozice[0] + object_offset, pozice[1] + object_offset)

class Hole(pygame.sprite.Sprite):
    def __init__(self, pozice):
        super().__init__()
        self.image = pygame.image.load("tank.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (object_size, object_size))
        self.rect = self.image.get_rect(topleft=(pozice[0] + object_offset, pozice[1] + object_offset))

holes = pygame.sprite.Group()
for pozice in grid:
    holes.add(Hole(pozice))


mole = Mole()
mole_group = pygame.sprite.GroupSingle(mole)

score = 0
timer = pygame.time.get_ticks()
visible_time = 450
game_active = False
streak = 0
game_over = False
miss_streak = 0

# Herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_active:
                if mole.rect.collidepoint(event.pos):
                    streak += 1  
                    miss_streak = 0
                    if streak >= 2:
                        score += 2  
                        damage_2.play()
                    else:
                        score += 1
                        damage_1.play()
                    mole.new_position()
                    timer = pygame.time.get_ticks()
                else:
                    streak = 0
                    miss_streak += 1
                    if miss_streak >= 10:
                        game_active = False
                        game_over = True
                        bg_music.stop()
                        prohra.play()
                        prohra2.play()
    else:
        game_active = True
        if not pygame.mixer.get_busy():
            bg_music.play(-1)
    if game_active:
        if score < 5:
            visible_time = 800
        
        elif score < 10:
            visible_time = 600
          
        elif score < 15:
            visible_time = 450

        else:
            visible_time = 300
            
        screen.blit(background_image, (0, 0))
       
        holes.draw(screen)
        mole_group.draw(screen)

        if pygame.time.get_ticks() - timer > visible_time:
            mole.new_position()
            timer = pygame.time.get_ticks()

        score_surface = text_font.render(f"Skóre: {score}", True, (255, 255, 255))
        screen.blit(score_surface, (20, 20))

    elif game_over:
        screen.blit(background_image, (0, 0))

        game_over_img = pygame.image.load("logo.png").convert_alpha()
        game_over_img = pygame.transform.scale(game_over_img, (300, 300))  # zmenšení loga
        screen.blit(game_over_img, (
            window_width // 2 - game_over_img.get_width() // 2,
            window_height // 2 - game_over_img.get_height() // 2
        ))

        game_over_text = text_font.render("PAIDAR ZNIČIL ŠKOLU", True, (255, 0, 0))
        screen.blit(game_over_text, (
            window_width // 2 - game_over_text.get_width() // 2,
            40
        ))
    pygame.display.update()
    clock.tick(60)
