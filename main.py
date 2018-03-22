import pygame
import pygame.camera
from pygame.locals import *
import tiles
from tiles import *


tileSide = 4
pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode(((240*tileSide),(288*tileSide)))
CLOCK = pygame.time.Clock()
TARGET_FPS=30
done = False
is_Color = True

x=30
y=30
speed=5
drawn = True
roomdraw = True
isblack = True
color = (151,128,158)
bg = (245,245,245)


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
						pygame.draw.rect(screen,(tileColor[p][k]),((z*tileSide)+(k*(40*tileSide)),(y*tileSide)+(p*(24*tileSide)),tileSide,tileSide))
					elif n == 0:
						pygame.draw.rect(screen,(grey),((z*tileSide)+(k*(40*tileSide)),(y*tileSide)+(p*(24*tileSide)),tileSide,tileSide))
		if p == 11:
			drawn = False

def reDraw():
	global tileSide
	global roomdraw
	global x
	global y 
	for p in range(0,12):
		for k in range(0,6):
			if (x>=(k*(40*tileSide)) and x<=((k+1)*(40*tileSide))) and (y>=(p*(24*tileSide)) and y<=((p+1)*(24*tileSide))):
				print(p,k)
				Map = order[p][k]
				for t in range(0,len(Map)):
					for z in range(0,len(Map[t])):
						n = Map[t][z]
						if n == 1: 
							pygame.draw.rect(screen,(tileColor[p][k]),((z*tileSide)+(k*(40*tileSide)),(t*tileSide)+(p*(24*tileSide)),tileSide,tileSide))
						elif n == 0:
							pygame.draw.rect(screen,(grey),((z*tileSide)+(k*(40*tileSide)),(t*tileSide)+(p*(24*tileSide)),tileSide,tileSide))
			roomdraw = False

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
	global roomdraw
	if KEYS['d']:
		x += speed
		roomdraw = True
	if KEYS['a']:
		x -= speed
		roomdraw = True
	if KEYS['s']:
		y += speed
		roomdraw = True
	if KEYS['w']:
		y -= speed
		roomdraw = True

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

	if isblack == True:
		screen.fill(bg)
		isblack = False
	if drawn == True:		
		mapDraw()
	if roomdraw == True:
		reDraw()
	pygame.draw.rect(screen,color,pygame.Rect(x,y,tileSide*1.5,tileSide*1.5))
	movement()
	CLOCK.tick(TARGET_FPS)
	pygame.display.flip()
