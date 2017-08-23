id = 0
print "id\twkt"
for x in xrange(-180,180,10):
	for y in xrange(-90,90,10):
		print "%d\tPOLYGON ((%d %d, %d %d, %d %d, %d %d, %d %d))" % (id,x,y,x+10,y,x+10,y+10,x,y+10,x,y)
		id += 1

