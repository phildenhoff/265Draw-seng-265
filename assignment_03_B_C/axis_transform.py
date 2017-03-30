"""Write to stdout a series of copies of the input shape along the x axis on both sides of the
    original shape and scales the size by half everytime"""
import sys
import copy
import Line_Point

DEFCOLOUR = "BlueViolet"

def draw(lines, delta_x):
    """draws copies of the shape along the x axis smaller everytime"""
    lines = copy.deepcopy(lines)

    for line in lines:
        line.scale(0.5)
        line.translate(delta_x, 0.0)
        line.translate(-delta_x, 0.0)
        print 'line', line

    return

def offset(size_given):
    """Return size of object plus constant 125."""
    return size_given + 125

def load_line_files(file_object):
    """Convert file_object to line_object."""
    lines = []
    for line in file_object:
        lineObject = line.split()
        point0 = Line_Point.Point(float(lineObject[1]), float(lineObject[2]))
        point1 = Line_Point.Point(float(lineObject[3]), float(lineObject[4]))
    try:
        colour = lineObject[5]
    except IndexError:
        colour = DEFCOLOUR
        lineObject = Line_Point.Line(point0, point1, colour)

        lines.append(lineObject)
    return lines

if len(sys.argv) != 2:
    print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' size of shape'
    sys.exit(1)

try:
    size = int(sys.argv[1])
except ValueError:
    print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' size of shape'
    sys.exit(2)

SHAPE = load_line_files(sys.stdin)
size = offset(size)

for originalline in SHAPE:
    print'line', originalline

#for i in range(n): # Is this supposed to be what the user picks?s
for i in range(size):
    draw(SHAPE, size)
