import sys
import math
import Line_Point

'''
purpose
	write to stdout a circle with radius n and radius scale factor f
preconditions
	n is a positive integer
	f is a floating point numbers
'''

def next_circle(root, f):
	# copy circle
	new_circle = Line_Point.Line(root.point0, root.point1)

	# translate to origin
	new_circle.translate(-root.point0.x, -root.point0.y)

	#scale
	new_circle.scale(f)

	# translate back
	new_circle.translate(root.point0.x, root.point0.y)

	# translate circle elsewhere
	new_circle.translate(root.point1.x - root.point0.x, root.point1.y - root.point0.y)

	return new_circle

def recursive_draw(root,h, f):
	# end recursion if base case reached
	if (h == 0):
		return

	# print root
	print 'line', root

	# continue with recursion
	recursive_draw( next_circle(root,f), h-1, a, f )
	recursive_draw( next_circle(root, f), h-1, a, f )

# ********** process the command line arguments

if len(sys.argv) != 4:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' height branch_angle branch_factor'
	sys.exit(1)
try:
	height = int(sys.argv[1])
	branch_angle = float(sys.argv[2])
	branch_factor = float(sys.argv[3])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' height branch_angle branch_factor'
	sys.exit(2)
if height < 1 or branch_factor <= 0:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' height branch_angle branch_factor'
	sys.exit(3)

# root: height 100, at bottom of canvas
point0 = Line_Point.Point(0.0,-250.0)
point1 = Line_Point.Point(0.0,-150.0)
root = Line_Point.Line(point0, point1)

recursive_draw(root, height, branch_angle, branch_factor)
