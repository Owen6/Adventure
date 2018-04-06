require "tiles"
require "player"

function love.load()

end

function love.update(dt)
	player:move(dt)
end

function love.draw()
	love.graphics.setBackgroundColor(235,235,235)
	player:draw()
end