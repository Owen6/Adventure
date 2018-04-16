require "tiles"

--[[def mapDraw():
	global tileSide
	global drawn
	for p in range(0,12):
		for k in range(0,6):
			Map = order[p][k]
			for y in range(0,len(Map)):
				for x in range(0,len(Map[y])):
					n = Map[y][x]
					if n == 1: 
						pygame.draw.rect(screen,(tileColor[p][k]),((x*tileSide)+(k*(40*tileSide)),(y*tileSide)+(p*(24*tileSide)),tileSide,tileSide))
					elif n == 0:
						pygame.draw.rect(screen,(grey),(),(y*tileSide)+(p*(24*tileSide)),tileSide,tileSide))
		if p == 11:
			drawn = False
			]]

function map_draw()
	for i=1, 12 do 
		for v=1, 6 do 
			Map = order[i][v]
			for y=1, #Map do
				for x=1, #Map[y] do
					n = Map[y][x]
					if n==1 then
						love.graphics.setColor(tileColor[i][v])
    					love.graphics.rectangle('fill', (x*tileSide)+(v*(20*tileSide)),(y*tileSide)+(i*(12*tileSide)),tileSide,tileSide)
					elseif n == 0 then
						love.graphics.setColor(grey)
						love.graphics.rectangle('fill', (x*tileSide)+(v*(20*tileSide)),(y*tileSide)+(i*(12*tileSide)),tileSide,tileSide)
					end
				end
			end
		end 
	end
end