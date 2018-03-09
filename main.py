import pygame
import pygame.camera
import tiles
from tiles import *



pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode((960,1080))
CLOCK = pygame.time.Clock()
TARGET_FPS=30
done = False

is_Color = True

"""with open('map.txt') as f:
	tiles = list(f)
print(tiles)"""
tileSide = 5
x=30
y=30
speed=5
drawn = True
black = False

KEYS = {
	"w" : False,
	"a" : False,
	"s" : False,
	"d" : False
}

def mapDraw():
	global tileSide
	global drawn
	for p in range(0,12):
		for k in range(0,6):
			Map = order[p][k]
			for y in range(0,len(Map)):
				for z in range(0,len(Map[y])):
					n = Map[y][z]
					if n == 1: 
						pygame.draw.rect(screen,(255,234,12),((z*tileSide)+(k*160),(y*tileSide)+(p*90),tileSide,tileSide))
					elif n == 0:
						pygame.draw.rect(screen,(178,178,178),((z*tileSide)+(k*160),(y*tileSide)+(p*90),tileSide,tileSide))
		print(p)
		if p == 11:
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
	global drawn
	if KEYS['d']:
		x += speed
		drawn = True
	if KEYS['a']:
		x -= speed
		drawn = True
	if KEYS['s']:
		y += speed
		drawn = True
	if KEYS['w']:
		y -= speed
		drawn = True

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
	if black == True:
		screen.fill(bg)
		black = False
	if drawn == True:		
		mapDraw()
	pygame.draw.rect(screen,color,pygame.Rect(x,y,7,7))
	movement()

	CLOCK.tick(TARGET_FPS)
	pygame.display.flip()

	