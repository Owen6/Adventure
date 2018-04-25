require "tiles"

function map_draw()
	for i=1, 12 do 
		for v=1, 6 do 
			Map = order[i][v]
			for y=1, #Map do
				for x=1, #Map[y] do
					n = Map[y][x]
					if n==1 then
						love.graphics.setColor(tileColor[i][v])
    					love.graphics.rectangle('fill', ((x-1)*tileSide)+((v-1)*(20*tileSide)),((y-1)*tileSide)+((i-1)*(12*tileSide)),tileSide,tileSide)
   					elseif n==4 or n==6  then
   						if n==4 then
    						love.graphics.setColor(grey)
							love.graphics.rectangle('fill', ((x-1)*tileSide)+((v-1)*(20*tileSide)),((y-1)*tileSide)+((i-1)*(12*tileSide)),tileSide,tileSide)
						end
						love.graphics.setColor(tileColor[i][v])
    					love.graphics.rectangle('fill', (((x-1)*tileSide)+((v-1)*(20*tileSide))),((y-1)*tileSide)+((i-1)*(12*tileSide)),tileSide/2,tileSide)
    				elseif n==5 or n==2 then
    					if n==5 then
    						love.graphics.setColor(grey)
							love.graphics.rectangle('fill', ((x-1)*tileSide)+((v-1)*(20*tileSide)),((y-1)*tileSide)+((i-1)*(12*tileSide)),tileSide,tileSide)
						end
						love.graphics.setColor(tileColor[i][v])
    					love.graphics.rectangle('fill', (((x-1)*tileSide)+((v-1)*(20*tileSide))+(tileSide/2)),((y-1)*tileSide)+((i-1)*(12*tileSide)),tileSide/2,tileSide)
					elseif n == 0 then
						love.graphics.setColor(grey)
						love.graphics.rectangle('fill', ((x-1)*tileSide)+((v-1)*(20*tileSide)),((y-1)*tileSide)+((i-1)*(12*tileSide)),tileSide,tileSide)
					end
				end
			end
		end 
	end
end	
