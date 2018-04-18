require "tiles"

player = {
	x = 30,
	y = 30,
	side = tileSide*1.25,
	speed = 300,
}

function player:move(dt)
	if love.keyboard.isDown('a') then
		self.x = self.x - self.speed*dt
	end
	if love.keyboard.isDown('d') then
		self.x = self.x + self.speed*dt
	end
	if love.keyboard.isDown('s') then
		self.y = self.y + self.speed*dt
	end
	if love.keyboard.isDown('w') then
		self.y = self.y - self.speed*dt
	end
end

function player:draw()
	love.graphics.setColor(0,0,0)
    love.graphics.rectangle('fill', self.x, self.y, self.side, self.side)
end