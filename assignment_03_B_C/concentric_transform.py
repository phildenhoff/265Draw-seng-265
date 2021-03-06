"""
Generate a shape (circle) with two of itself, half the radius, inside - touching exactly at the
radius of the outer circle and the center of the circle.
"""
import sys
import math
import copy
import Line_Point

DEFCOLOUR = "BlueViolet"

def drawConcentric(lines, angle, index):
    """Draw a shape based on its index and angle."""
    lines = copy.deepcopy(lines)
    # print newly rotated items
    for line in lines:
        line.scale(0.5)
        line.translate(0.0, 125.0)
        line.rotate(angle*index)
        print 'line', line
    return

def generateOffset(numInnerShapes):
    """Returns angle in radians between each shape."""
    if (numInnerShapes == 0): return 0
    return float(2*math.pi / numInnerShapes)

def loadLineFile(fileObject, colour=DEFCOLOUR):
    """Convert lines of text from file object into list of Line objects.
    Returns:
        Line list - all line objects in file.
    """
    lines = []
    for line in fileObject:
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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >> sys.stderr, 'Syntax: %s [number of inner shapes]' %sys.argv[0]
        sys.exit(1)
    try:
        NUMINNERSHAPES = int(sys.argv[1])
    except ValueError:
        print >> sys.stderr, 'Syntax: %s [number of inner shapes]' %sys.argv[0]
        sys.exit(1)

    SHAPE = loadLineFile(sys.stdin)
    SHAPEOFFSET = generateOffset(NUMINNERSHAPES)
    # print original shape

    for originalLine in SHAPE:
        print 'line', originalLine

    for i in range(NUMINNERSHAPES):
        drawConcentric(SHAPE, SHAPEOFFSET, i)
