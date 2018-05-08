require "tiles"
keypic = love.graphics.newImage('key.png')
key1 = false
key = {
	name = "key",
	x = 245,
	y = 250,
	width = keypic:getWidth()*.055,
	height = keypic:getHeight()*.055
}

castlegate1 = {
	name = "gate1",
	x = 276,
	y = 276,
	w = 8
}

function key_draw()
	love.graphics.setColor(yellow)
	love.graphics.draw(keypic,key.x,key.y, 0, .065, .065)
end