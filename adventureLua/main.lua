require "tiles"
require "player"
require "map"

function love.load()

end

function love.update(dt)
	player:move(dt)
end

function love.draw()
	love.graphics.setBackgroundColor(235,235,235)
	map_draw()
	player:draw()
end