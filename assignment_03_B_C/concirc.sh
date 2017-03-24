#/bin/bash
# usage: concirc.sh
#   options:
#       [-l number of levels down]
#       [ valid css colors (unlimited number)]
#       [-n inner concentric circle number]

verbose='false'
levels='' # how many times to do the operations
n='' # how many objects to put on each level
cflag='' # whether colors have been listed
color=''

usage() {
 >&2 echo -e "Usage: concirc.sh [ -l number of levels] [-n number of inner circles] [ -c valid css colors ]
Excluding any one argument will set it to the default:
\tl = 3
\tn = 3
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
while getopts 'hl:n:cv' flag; do
    case ${flag} in
	h) usage ;;
        l) levels="${OPTARG}" ;;
        n) n="${OPTARG}"  ;;
        c) cflag='true' ;;
        v) verbose='true' ;;
	*) usage ;;
    esac
done
shift $(( OPTIND - 1))

# If cflag set, get colors from arguments
if [ "$cflag" == 'true' ]; then
 for color in "$@"; do
  colors+="$color "
 done
fi

# Setting default values
if [ "$levels" == '' ]; then
  levels=3
fi
if [ "$n" == '' ]; then
  n=3
fi
if [ "$cflag" == '' ]; then
  colors="Black"
fi

if [ "$verbose" == 'true' ]; then
 echo -e "Levels: $levels \nObjects per level: $n \nColors: $colors"
fi

# generating images
python generate_polygon.py 250 0 10000 > k1.txt
python lines_to_svg_colour.py k1.txt > k1.svg
