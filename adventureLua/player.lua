require "tiles"

local function collisionfilter(item,other)
	if other.name == "key" then
		return "cross"
	end
	if other.name == "gate1" and key1 then
		return "cross"
	end
	return "slide"
end

player = {
	x = 278.5,
	y = 278,
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
	local nextX, nextY, cols, len = world:move(self, futureX, futureY,collisionfilter)

	for i=1, len do
		local col = cols[i]
		if col.other.name == "key" then
			key1 = 'true'
		end
	end

	self.x = nextX
	self.y = nextY
end

function player:draw()
	love.graphics.setColor(0,0,0)
    love.graphics.rectangle('fill', self.x, self.y, self.side, self.side)
end