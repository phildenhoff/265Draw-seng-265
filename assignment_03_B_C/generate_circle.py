import sys
import math
import Line_Point_colour
# pylint: disable=all

'''
purpose
	write to stdout a concentric circle with colour range cr, concentric layers l, and starting colour c
preconditions
    l is a positive integer
    cr is a positive integer less than or equal to l
    c is a valid colour string from css_colour.txt
'''

def draw_circle(circletop,colour,s):
	central_angle = 2 * math.pi / s
	c0 = Line_Point_colour.Point(xcoord,ycoord)
	while s > 0:
		c1 = Line_Point_colour.Point(c0.x, c0.y)
		c1.rotate(central_angle)
		print 'line', Line_Point_colour.Line(c0, c1)
		c0 = c1
		s = s - 1

	return new_circle

def recursive_draw(circletop,n,l,s):
	# end recursion if base case reached
	if (l == 0 or s==0):
		return

	# print root
	print 'line', circletop

	# continue with recursion
	recursive_draw( draw_circle(circletop,colour,s), l-1,s/2)
	recursive_draw( draw_circle(circletop,colour,s), l-1,s/2)
	recursive_draw( draw_circle(circletop,colour,s), l-1,s/2)
	recursive_draw( draw_circle(circletop,colour,s), l-1,s/2)

# ********** process the command line arguments

if len(sys.argv) != 4:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' layers colourRange colour '
	sys.exit(1)
try:
	layers = int(sys.argv[1])
	colourRange = int(sys.argv[2])
	colour = str(sys.argv[3])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' layers colourRange colour '
	sys.exit(2)
if layers < 1 or colourRange > layers:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' layers colourRange '
	sys.exit(3)

# starting point: x-175 y-175 , at top of canvas
s = 2000
x0 = float(175)
y0 = float(175)
central_angle = 2 * math.pi / s
p0 = Line_Point_colour.Point(x0,y0)
while s > 0:
	p1 = Line_Point_colour.Point(p0.x, p0.y)
	p1.rotate(central_angle)
	print 'line', Line_Point_colour.Line(p0, p1,colour)
	p0 = p1
	s = s - 1

recursive_draw(p0, layers,colour,s)
