id = 0
print "id\twkt"
for x in xrange(-180,180,10):
	for y in xrange(-90,90,10):
		print "%d\tMULTIPOINT ((%d %d), (%d %d), (%d %d), (%d %d))" % (id,x,y,x+10,y,x,y+10,x+10,y+10)
		id += 1

