import pygame
pygame.init()
screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption("Basketball Flipper")
circle_x = 20
circle_y = 40
circle_x_direction = 2
circle_y_direction = 2
timer = pygame.time.Clock()
framerate = 60
score = 0
border1 = pygame.Rect(0, 0, 300, 10)
border2 = pygame.Rect(290, 0, 10, 500)
border3 = pygame.Rect(0, 0, 10, 500)
border4 = pygame.Rect(10, 490, 280, 10)
flipper_x = 100
flipper = pygame.Rect(flipper_x, 480, 100, 10)

move_left = False
move_right = False


def ScreenText(text, color, x, y, size, style):
    font = pygame.font.SysFont(style, size, bold=True, italic=True)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))


def flipper_hit():
    if ball.colliderect(flipper_init):
        global circle_y_direction
        circle_y_direction *= -1


def lose():
    if ball.colliderect(frame4):
        global running
        running = False

def restart():
    pass


def score_update():
    global score
    if ball.colliderect(flipper_init):
        score += 1

def update_speed():
    global circle_y_direction
    circle_y_direction += 0.05
    int(circle_y_direction)


running = True
while running:
    timer.tick(framerate)
    circle_x += circle_x_direction
    circle_y += circle_y_direction
    if circle_y < 20 or circle_y > 480:
        circle_y_direction *= -1
    if circle_x < 20 or circle_x > 280:
        circle_x_direction *= -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right:
        if flipper_x < 190:
            flipper_x += 5
            flipper.x = flipper_x
    if move_left:
        if flipper_x > 10:
            flipper_x -= 5
            flipper.x = flipper_x
    screen.fill((0, 0, 0))
    ball = pygame.draw.circle(screen, (255, 255, 255),
                              (circle_x, circle_y), 10, 5)
    frame1 = pygame.draw.rect(
        surface=screen, color=(255,72,196), rect=border1)
    frame2 = pygame.draw.rect(
        surface=screen, color=(255,72,196), rect=border2)
    frame3 = pygame.draw.rect(
        surface=screen, color=(255,72,196), rect=border3)
    frame4 = pygame.draw.rect(surface=screen, color="red", rect=border4)
    flipper_init = pygame.draw.rect(
        surface=screen, color=(43,209,252), rect=flipper, border_radius=40)
    ScreenText(f"Score: {score}", (43,209,252), 105, 20, size=20, style="Comic Sans")
    ScreenText(f"Best score: 0", (43,209,252), 105, 40, size=15, style="Comic Sans")
    flipper_hit()
    lose()
    score_update()
    update_speed()
    pygame.display.flip()

pygame.quit()
