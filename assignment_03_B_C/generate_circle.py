import sys
import math
import Line_Point_colour


'''
purpose
	write to stdout a concentric circle with colour range cr, concentric layers l, and starting colour c
preconditions
    l is a positive integer
    cr is a positive integer less than or equal to l
    c is a valid colour string from css_colour.txt
'''

def draw_circle(circletop,colour,sides,count):
	if count == 4:
		central_angle = 2 * math.pi / sides
		new_circle = Line_Point_colour.Point(circletop.x,circletop.y)
		new_circle.translate(circletop.x,circletop.y)
		while sides > 0:
			new_c1 = Line_Point_colour.Point(new_circle.x, new_circle.y)
			new_c1.rotate(central_angle)
			print 'line', Line_Point_colour.Line(new_circle, new_c1)
			new_circle = new_c1
			sides = sides - 1
	if count == 3:
		central_angle = 2 * math.pi / sides
		new_circle = Line_Point_colour.Point(circletop.x,circletop.y)
		new_circle.translate(circletop.x,float(circletop.y-circletop.y/2))
		while sides > 0:
			new_c1 = Line_Point_colour.Point(new_circle.x, new_circle.y)
			new_c1.rotate(central_angle)
			print 'line', Line_Point_colour.Line(new_circle, new_c1)
			new_circle = new_c1
			sides = sides - 1
	if count == 2:
		central_angle = 2 * math.pi / sides
		new_circle = Line_Point_colour.Point(circletop.x,circletop.y)
		new_circle.translate(float(-(circletop.y/4)),float(circletop.y*(3/4)))
		while sides > 0:
			new_c1 = Line_Point_colour.Point(new_circle.x, new_circle.y)
			new_c1.rotate(central_angle)
			print 'line', Line_Point_colour.Line(new_circle, new_c1)
			new_circle = new_c1
			sides = sides - 1
	if count == 1:
		central_angle = 2 * math.pi / sides
		new_circle = Line_Point_colour.Point(circletop.x,circletop.y)
		new_circle.translate(float(circletop.y/4),float(circletop.y*(3/4)))
		while sides > 0:
			new_c1 = Line_Point_colour.Point(new_circle.x, new_circle.y)
			new_c1.rotate(central_angle)
			print 'line', Line_Point_colour.Line(new_circle, new_c1)
			new_circle = new_c1
			sides = sides - 1
	else:
		return


def recursive_draw(circletop, layer, colour, sides):
	# end recursion if base case reached
	if layer == 0 or sides==0:
		return

	# print circletop
	print 'line', circletop

	count = 4
	sides = sides/2

	# continue with recursion
	recursive_draw(draw_circle(circletop/2,colour,sides,count),layer-1,colour,sides)
	'''
	recursive_draw( draw_circle(circletop/2,colour,s/2,count-1), l-1,colour,s/2)
	recursive_draw( draw_circle(circletop/2,colour,s/2,count-2), l-1,colour,s/2)
	recursive_draw( draw_circle(circletop/2,colour,s/2,count-3), l-1,colour,s/2)
	'''

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

# starting point: x-0 y-176 , at top of canvas
s = 2000
x0 = float(0)
y0 = float(248)
central_angle = 2 * math.pi / s
p0 = Line_Point_colour.Point(x0,y0)
while s > 0:
	p1 = Line_Point_colour.Point(p0.x, p0.y)
	p1.rotate(central_angle)
	print 'line', Line_Point_colour.Line(p0, p1,colour)
	p0 = p1
	s = s - 1

recursive_draw(p0, layers,colour,s)
