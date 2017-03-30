#/bin/bash
# usage: concirc.sh
#   options:
#       [ -l number of levels down]
#       [ -c valid css color]
#       [ -n inner concentric circle number]
#	[ -y number of inner shapes]

verbose='false'
levels='' # how many times to do the operations
n='' # how many objects to put on each level
cflag='' # whether colors have been listed
color=''
y='' # number of different colours to use

usage() {
 >&2 echo -e "Usage: concirc.sh [ -l number of levels] [-n number of inner shapes] [-y number of colors to cycle through] [ -c valid css color ]
Excluding any one argument will set it to the default:
\tl = 3
\tn = 3
\ty = 2
\tc = Black"
 echo -e "Using concirc.sh -h will bring up this manual." >&2
 exit 1
}

# Handling no arguments given
if [ $# -lt 1 ]; then
  echo "Error: Too few arguments" 1>&2
  usage
fi

# Handle given arguments
while getopts 'hl:n:c:vy:' flag; do
    case ${flag} in
	h) usage ;;
        l) levels="${OPTARG}" ;;
        n) n="${OPTARG}"  ;;
        # c) cflag='true' ;; # multi colour support
	c) color="${OPTARG}" ;;
        v) verbose='true' ;;
	y) y="${OPTARG}" ;; 
	*) usage ;;
    esac
done
shift $(( OPTIND - 1))

# multi colour support
## If cflag set, get colors from arguments
#if [ "$cflag" == 'true' ]; then
# for color in "$@"; do
#  colors+="$color "
# done
#fi

# Setting default values
if [ "$levels" == '' ]; then
  levels=3
fi
if [ "$n" == '' ]; then
  n=3
fi
if [ "$color" = '' ]; then
  color="Black"
fi
if [ "$y" == '' ]; then
  y=2
fi

if [ "$verbose" == 'true' ]; then
 echo -e "Levels: $levels \nObjects per level: $n \nNumber of colors: $y \nColor: $color"
fi

# generating circle
if [ "$verbose" == 'true' ]; then
  echo "Generating lines files"
fi
python generate_circle.py $levels $y $color > k1.txt
python concentric_transform.py $y < k1.txt > k2.txt
if [ "$verbose" == 'true' ]; then
  echo "Generating SVG from text files"
fi
python lines_to_svg_colour.py k2.txt > concirc.svg
if [ "$verbose" != 'true' ]; then
  rm k1.txt k2.txt
else
  echo "Not removing text files due to verbose mode"
fi
