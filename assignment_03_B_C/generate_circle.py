import sys
import math
import Line_Point_colour
# pylint: disable=W0312

'''
purpose
	write to stdout a concentric circle with colour range cr, concentric layers l, and starting colour c
preconditions
    l is a positive integer
    cr is a positive integer less than or equal to l
    c is a valid colour string from css_colour.txt
'''

def draw_circle(circletop, layer, spacing, cr, sides):
	if sides == 0:
		return
	sides = sides*(1-layer*1/10)
	central_angle = 2 * math.pi / sides
	new_x0 = float(0)
	new_y0 = float(248-spacing*layer)
	if new_y0 == 0:
		new_y0 = float(248)
	new_circle = Line_Point_colour.Point(new_x0, new_y0)
	while sides > 0:
		new_c1 = Line_Point_colour.Point(new_circle.x, new_circle.y)
		new_c1.rotate(central_angle)
		print 'line', Line_Point_colour.Line(new_circle, new_c1, cr)
		new_circle = new_c1
		sides = sides - 1
	return new_circle

def recursive_draw(circletop, layer, spacing, cr, sides):
	# end recursion if base case reached
	if layer == 0 or sides == 0:
		return
	# continue with recursion
	recursive_draw(draw_circle(circletop, layer, spacing, cr, sides), layer-1, spacing, cr, sides)
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

# starting point: x- 0 y- 248 , at top of canvas
x0 = float(0)
y0 = float(248)
s = 2000
spacing = 248/layers
circletop = Line_Point_colour.Point(x0, y0)
recursive_draw(circletop, layers, spacing, colour, s)
