#!/usr/local/bin/lua

function elementIterator( collection )
	-- body
	local index = 0
	local count = #collection
	return function()
		index = index + 1
		if index<=count then
			return collection[index]
		end
	end
end

for e in elementIterator({"a","b","c"})
	do
	print(e)
end


