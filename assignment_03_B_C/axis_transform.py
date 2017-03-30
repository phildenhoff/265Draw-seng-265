import sys
import math
import copy
import Line_Point

"""writes to stdout a series of copies of the input shape along the x axis on both sides of the original shape and scales the size by half everytime"""

def draw(lines,delta_x, n)
	"draws copies of the shape along the x axis smaller everytime"
	lines = copy.deepcopy(lines)

	for line in lines:
		line.scale(0.5)
		line.translate(delta_x, 0.0)
		line.translate(-delta_x, 0.0)
		print 'line', line

	return

def Offset(size)
	return size + 125

def load_line_files(file_object)
	line_object = [ ]
	for line in file_object:
		point0 = Line_Point.Point(float(line_object[1]),float(line_object[2])
		point1 = Line_Point.Point(float(line_object[3]),float(line_object[4])
		line_object = Line_Point.Point(point0, point1)

		line_object.append(line_object)

	return line_object

if len(sys.argv) != 2:
	print >> sys.stdrr, 'Syntax: ' + sys.argv[0] + 'size of shape'
	sys.exit(1)

try:
	size = int(sys.argv[1])

except: ValueError
	print >> sys.drr, 'Syntax: ' + sys.argv[0] + 'size of shape'
	sys.exit(2)

SHAPE = load_line_file(sys.stdin)
size = Offset(size)

for originalline in SHAPE:
	print'line', originalline

for i in range(n):
	draw(SHAPE, size, i)
