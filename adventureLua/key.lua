
key = {
	name = "key",
	x = 0,
	y = 0
}
keypic = love.graphics.newImage('key.png')

function key_draw()
	love.graphics.draw(keypic,90,110, 0, .065, .065)
end