require "tiles"

player = {
	x = 90,
	y = 110,
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

	local futureX = self.x + self.xvel * dt
	local futureY = self.y + self.yvel * dt
	local nextX, nextY, cols, len = world:move(self, futureX, futureY)
	self.x = nextX
	self.y = nextY
end

function player:draw()
	love.graphics.setColor(0,0,0)
    love.graphics.rectangle('fill', self.x, self.y, self.side, self.side)
end