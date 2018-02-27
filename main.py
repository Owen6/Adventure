import pygame

pygame.init()
screen = pygame.display.set_mode((700,700))
CLOCK = pygame.time.Clock()
TARGET_FPS=60
done = False

is_Color = True

with open('map.txt') as f:
	words = list(f)

x=30
y=30
speed=5

KEYS = {
	"w" : False,
	"a" : False,
	"s" : False,
	"d" : False
}

def keyswitch(key,boolv):
	if key == pygame.K_d:
		KEYS['d'] = boolv
	if key == pygame.K_a:
		KEYS['a'] = boolv
	if key == pygame.K_s:
		KEYS['s'] = boolv
	if key == pygame.K_w:
		KEYS['w'] = boolv

def movement():
	global x
	global y
	if KEYS['d']:
		x += speed
	if KEYS['a']:
		x -= speed
	if KEYS['s']:
		y += speed
	if KEYS['w']:
		y -= speed

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			is_Color = not is_Color
		if event.type == pygame.KEYDOWN:
			keyswitch(event.key, True)
		if event.type == pygame.KEYUP:
			keyswitch(event.key, False)
	if is_Color:
		color = (151,128,158)
		bg = (0,0,0)
	else:
		color = (104,127,97)
		bg = (255,255,255)
	screen.fill(bg)
	pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))
	movement()

	CLOCK.tick(TARGET_FPS)
	pygame.display.flip()