require "tiles"

player = {
	x = 30,
	y = 30,
	side = tileSide*.75,
	speed = 100,
	xvel = 0,
	yvel = 0
}

function player:move(dt)
	if love.keyboard.isDown('a') then
		self.xvel = -self.speed
	elseif love.keyboard.isDown('d') then
		self.xvel = self.speed
	else
		self.xvel = 0
	end
	if love.keyboard.isDown('s') then
		self.yvel = self.speed
	elseif love.keyboard.isDown('w') then
		self.yvel = -self.speed
	else
		self.yvel = 0
	end

	self.x = self.x + self.xvel * dt
	self.y = self.y + self.yvel * dt
end

function player:draw()
	love.graphics.setColor(0,0,0)
    love.graphics.rectangle('fill', self.x, self.y, self.side, self.side)
end