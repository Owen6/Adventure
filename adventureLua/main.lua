local bump = require "bump"
world = bump.newWorld()
require "tiles"
require "player"
require "map"
require "key"
camera = require "camera"
local cam = camera(0,0)
menu = true

function love.load()
	cam:zoomTo(6)
	world:add(player, player.x, player.y, player.side, player.side)
	world:add(key,key.x,key.y,key.width,key.height)
	world:add(castlegate1,castlegate1.x,castlegate1.y-1,castlegate1.w,1)
	for i=1, 12 do 
		for v=1, 6 do 
			Map = order[i][v]
			for y=1, #Map do
				for x=1, #Map[y] do
					n = Map[y][x]
					if n==1 then
						local block = {
							x = ((x-1)*tileSide)+((v-1)*(20*tileSide)),
							y = ((y-1)*tileSide)+((i-1)*(12*tileSide)),
							width = tileSide,
							height = tileSide,
						}
						world:add(block, block.x, block.y, block.width, block.height)
					elseif n==2 or n==6 then
						local block = {
							x = ((x-1)*tileSide)+((v-1)*(20*tileSide)),
							y = ((y-1)*tileSide)+((i-1)*(12*tileSide)),
							width = tileSide,
							height = tileSide,
						}
						world:add(block, block.x, block.y, block.width, block.height)
					elseif n==4 then
						local block = {
							x = ((x-1)*tileSide)+((v-1)*(20*tileSide)),
							y = ((y-1)*tileSide)+((i-1)*(12*tileSide)),
							width = tileSide/2,
							height = tileSide,
						}
						world:add(block, block.x, block.y, block.width, block.height)
					elseif n==5 then
						local block = {
							x = ((x-1)*tileSide)+((v-1)*(20*tileSide))+(tileSide/2),
							y = ((y-1)*tileSide)+((i-1)*(12*tileSide)),
							width = tileSide/2,
							height = tileSide,
						}
						world:add(block, block.x, block.y, block.width, block.height)
					end
				end
			end
		end 
	end
end

function love.update(dt)
	local cx,cy = 0,0
	for i=1, 12 do 
		for v=1, 6 do
			if player.x >= (v*(20*tileSide)) and player.x <= ((v+1)*(20*tileSide)) then
				cx = v
			end
			if  player.y >= (i*(12*tileSide)) and player.y <= ((i+1)*(12*tileSide)) then
				cy = i
			end
		end
	end
	cam:lookAt(cx*(20*4)+ (20*2),cy*(12*4))
	player:move(dt)
end

function love.draw()
	if menu == false then
		cam:attach()
		love.graphics.setBackgroundColor(235,235,235)
		map_draw()
		if key1 == false then
			key_draw()
		end
		player:draw()
--[[		
		local items, len = world:getItems()
		for i = 1, len do
			local item = items[i]
			love.graphics.setColor(1, 0, 0)
			love.graphics.rectangle("line", item.x, item.y, tileSide, tileSide)
		end
		]]
		cam:detach()
		if key1 then
			love.graphics.setColor(0,0,0)
			love.graphics.draw(keypic,395,540,0, 1, 1)
			print(key1 == true)
		end
			print(player.x,player.y)
	else
		menupic = love.graphics.newImage('atari.png')
		love.graphics.draw(menupic,0,0,0,2.35,2.4)
	end
end

function love.keypressed(key)
  if key == 'space' then 
  	menu = false
  end
end

function love.keyreleased(key)
  if key == 'escape' then
    love.event.quit()
  end
end