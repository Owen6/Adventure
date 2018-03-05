import pygame
import tiles
from tiles import *



pygame.init()
screen = pygame.display.set_mode((1920,2160))
CLOCK = pygame.time.Clock()
TARGET_FPS=60
done = False

is_Color = True

"""with open('map.txt') as f:
	tiles = list(f)
print(tiles)"""
tileSide = 10
x=30
y=30
speed=5
drawn = True

KEYS = {
	"w" : False,
	"a" : False,
	"s" : False,
	"d" : False
}

def mapDraw():
	global tileSide
	for p in range(0,12):
		for k in range(0,6):
			Map = order[p][k]
			for y in range(0,len(Map)):
				for z in range(0,len(Map[y])):
					n = Map[y][z]
					if n == 1: 
						pygame.draw.rect(screen,(255,234,12),((z*tileSide)+(k*320),(y*tileSide)+(p*180),tileSide,tileSide))
		print(p)
	drawn = False

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
	if drawn == True:
		mapDraw()
	pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))
	movement()

	CLOCK.tick(TARGET_FPS)
	pygame.display.flip()

	