require "tiles"
require "player"
require "map"
camera = require "camera"
local cam = camera(0,0)

function love.load()
	cam:zoomTo(6)

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
	cam:lookAt(cx*(20*4)+ (20*2),cy*(12*4)+ (12*2))
	player:move(dt)
end

function love.draw()
	cam:attach()
	love.graphics.setBackgroundColor(235,235,235)
	map_draw()
	player:draw()
	cam:detach()
end