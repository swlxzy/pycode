import pygame
import random
import time

# Pygame başlat
pygame.init()

# Ekran ayarları
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dinozor Oyunu")

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# FPS
clock = pygame.time.Clock()

# Oyuncu özellikleri
energy = 100
hunger = 100
health = 100
meat = 0
last_attack_time = time.time()

# Font ayarları
font = pygame.font.Font(None, 36)

# Dinozor bilgileri
player_dino = {"name": "Dracorex Hogwartsia", "strength": 70, "size": 3}
enemies = [
    {"name": "Zby", "strength": 50, "size": 2},
    {"name": "Raptorex", "strength": 40, "size": 1},
    {"name": "Psittacosaurus", "strength": 30, "size": 1},
    {"name": "Incisivosaurus", "strength": 20, "size": 1},
    {"name": "Pelecanimimus", "strength": 25, "size": 1},
]

# Bar çizim fonksiyonu
def draw_bar(x, y, value, color):
    pygame.draw.rect(screen, WHITE, (x, y, 200, 20))  # Arka plan bar
    pygame.draw.rect(screen, color, (x, y, 2 * value, 20))  # Doluluk oranı

# Ana oyun döngüsü
running = True
on_hunt_screen = False

while running:
    screen.fill(BLACK)

    # Etiketler
    energy_text = font.render(f"Enerji: {energy}/100", True, WHITE)
    hunger_text = font.render(f"Açlık: {hunger}/100", True, WHITE)
    health_text = font.render(f"Can: {health}/100", True, WHITE)
    meat_text = font.render(f"Et: {meat}", True, WHITE)

    # Barları çiz
    draw_bar(50, 50, energy, GREEN)
    draw_bar(50, 80, hunger, (255, 255, 0))
    draw_bar(50, 110, health, RED)

    # Etiketleri ekrana yazdır
    screen.blit(energy_text, (300, 50))
    screen.blit(hunger_text, (300, 80))
    screen.blit(health_text, (300, 110))
    screen.blit(meat_text, (50, 140))

    # Rastgele dinozor saldırı kontrolü
    if time.time() - last_attack_time > 240:  # 4 dakika
        energy -= 15
        health -= 10
        if energy < 0:
            energy = 0
        if health < 0:
            health = 0
        last_attack_time = time.time()
        print("Bir dinozor saldırısı oldu!")

    # Avlanma ekranı
    if on_hunt_screen:
        enemy_y = 200
        for enemy in enemies:
            enemy_text = font.render(enemy["name"], True, WHITE)
            screen.blit(enemy_text, (50, enemy_y))
            enemy_y += 50

    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if on_hunt_screen:
                # Avlanma ekranındaki dinozorlar
                enemy_index = (y - 200) // 50
                if 0 <= enemy_index < len(enemies):
                    enemy = enemies[enemy_index]
                    print(f"{enemy['name']} ile savaşıyorsunuz!")
                    energy -= enemy["strength"] // 2
                    hunger -= enemy["size"] * 10
                    meat += enemy["size"]
                    if energy < 0:
                        energy = 0
                    if hunger < 0:
                        hunger = 0
                    on_hunt_screen = False
            else:
                # Ana ekran işlemleri
                if 50 < x < 250 and 180 < y < 210:  # "Avlan" düğmesi
                    on_hunt_screen = True
                elif 50 < x < 250 and 240 < y < 270:  # "Et Ye" düğmesi
                    if meat >= 5:
                        meat -= 5
                        health += 2
                        if health > 100:
                            health = 100
                    if meat > 0:
                        energy += meat * 10
                        meat = 0
                        if energy > 100:
                            energy = 100

    # Düğmeleri çiz
    if not on_hunt_screen:
        pygame.draw.rect(screen, GREEN, (50, 180, 200, 30))  # Avlan düğmesi
        pygame.draw.rect(screen, GREEN, (50, 240, 200, 30))  # Et ye düğmesi

        hunt_text = font.render("Avlan", True, BLACK)
        eat_text = font.render("Et Ye", True, BLACK)
        screen.blit(hunt_text, (110, 185))
        screen.blit(eat_text, (110, 245))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
