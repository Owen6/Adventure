keypic = love.graphics.newImage('key.png')
key1 = false
key = {
	name = "key",
	x = 110,
	y = 110,
	width = keypic:getWidth()*.065,
	height = keypic:getHeight()*.065
}


function key_draw()
	love.graphics.setColor(1,1,1)
	love.graphics.draw(keypic,key.x,key.y, 0, .065, .065)
end