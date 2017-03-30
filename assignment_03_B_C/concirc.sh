#/bin/bash
# usage: concirc.sh
#   options:
#       [ -l number of levels down]
#       [ -c valid css color]
#       [ -n inner concentric circle number]
#	      [ -y number of inner shapes]

verbose='false'
levels='' # how many times to do the operations
n='' # how many objects to put on each level
cflag='' # whether colors have been listed
color=''
y='' # number of different colours to use

usage() {
  # Print an in-line help guide for the user
 >&2 echo -e "Usage: concirc.sh
\t[ -l number of levels < 10]
\t[ -n number of inner shapes]
\t[ -y number of colors to cycle through < l]
\t[ -c valid CSS color]
Excluding any one argument will set it to the default:
\tl = 3
\tn = 3
\ty = 2
\tc = Black
however, at least one argument must be used."
 echo -e "Using concirc.sh -h will bring up this manual." >&2
 exit 1
}

# Handling no arguments given
if [ $# -lt 1 ]; then
  echo "ERROR: Too few arguments" 1>&2
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

# Catch invalid operands
if [ "$levels" -ge 10 ]; then
  echo -e "ERROR: l must be less than 10." >&2
  usage
fi
if [ "$y" -gt "$levels" ]; then
  echo -e "ERROR: y must be less than l." >&2
  usage
fi

# If verbose, we print a "pre-flight check"
if [ "$verbose" == 'true' ]; then
 echo -e "Levels: $levels \nObjects per level: $n \nNumber of colors: $y \nColor: $color"
fi

# generating circle
if [ "$verbose" == 'true' ]; then
  echo "Generating lines files"
fi
python generate_circle.py $levels $y $color > k1.txt
# Error handling against invalid CSS colours
if [  "$?" -ne "0" ]; then
  # Error output from generate_circle.py
  usage
fi

# Transform around center
python concentric_transform.py $n < k1.txt > k2.txt

#Output image to svg
if [ "$verbose" == 'true' ]; then
  echo "Generating SVG from text files"
fi
python lines_to_svg_colour.py k2.txt > concirc.svg

if [ "$verbose" != 'true' ]; then
  rm k1.txt k2.txt
else
  echo "Not removing text files due to verbose mode"
fi
