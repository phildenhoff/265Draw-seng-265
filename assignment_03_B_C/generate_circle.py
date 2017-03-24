import sys
import math
import Line_Point
# pylint: disable=all

'''
purpose
	write to stdout a circle with radius n, colours c, concentric layers l, and inner circles i
preconditions
	n is a positive integer and less than or equal to 250
    l is a positive integer
    i is a positive integer
    c is a valid colour string from css_colour.txt
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

def recursive_draw(root,n,l,i):
	# end recursion if base case reached
	if (l == 0):
		return

	# print root
	print 'line', root

	# continue with recursion
	recursive_draw( next_circle(root,f), n, l-1, i )
	recursive_draw( next_circle(root,f), n, l-1, i )

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
s = 765
central_angle = 2 * math.pi / s
p0 = Line_Point.Point(x0, y0)
while s > 0:
	p1 = Line_Point.Point(p0.x, p0.y)
	p1.rotate(central_angle)
	print 'line', Line_Point.Line(p0, p1)
	p0 = p1
	s = s - 1

recursive_draw(root, height, branch_angle, branch_factor)
