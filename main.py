import pygame
import pygame.camera
from pygame.locals import *
import tiles
from tiles import *



pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode((960,1080))
CLOCK = pygame.time.Clock()
TARGET_FPS=30
done = False

is_Color = True

#class Capture(object):
#	def __init__(self):
#		self.size(960,480)
#		self.display = pygame.display.set_mode(self.size, 0)
#		self.clist = pygame.camera.list_cameras()
#		if not self.clist:
#			raise ValueError("No Cameras")
#		self.cam = pygame.camera.Camera(self.clist[0],self.size)
#		self.cam.start()
#		self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
#	def get

tileSide = 5
x=30
y=30
speed=5
drawn = True
roomdraw = True
isblack = True

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
						pygame.draw.rect(screen,(tileColor[p][k]),((z*tileSide)+(k*160),(y*tileSide)+(p*90),tileSide,tileSide))
					elif n == 0:
						pygame.draw.rect(screen,(grey),((z*tileSide)+(k*160),(y*tileSide)+(p*90),tileSide,tileSide))
		print(p)
		if p == 11:
			drawn = False

def reDraw():
	global tileSide
	global roomdrawn
	global x
	global y 
	for p in range(0,12):
		for k in range(0,6):
			if (x>=(k*160) and x<((k+1)*160)) and (y>=(p*160) and y<((p+1)*160)):
				Map = order[p][k]
				for t in range(0,len(Map)):
					for z in range(0,len(Map[t])):
						n = Map[t][z]
						if n == 1: 
							pygame.draw.rect(screen,(tileColor[p][k]),((z*tileSide)+(k*160),(t*tileSide)+(p*90),tileSide,tileSide))
						elif n == 0:
							pygame.draw.rect(screen,(grey),((z*tileSide)+(k*160),(t*tileSide)+(p*90),tileSide,tileSide))
		if p == 11:
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
	global drawn
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
	if is_Color:
		color = (151,128,158)
		bg = (255,255,255)
	else:
		color = (104,127,97)
		bg = (255,255,255)
	if isblack == True:
		screen.fill(bg)
		isblack = False
	if drawn == True:		
		mapDraw()
	if roomdraw == True:
		reDraw()
	pygame.draw.rect(screen,color,pygame.Rect(x,y,7,7))
	movement()

	CLOCK.tick(TARGET_FPS)
	pygame.display.flip()

	