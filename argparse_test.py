import argparse
from help_formatter import SingleMetavarHelpFormatter

parser = argparse.ArgumentParser(
    prog='SubtitleJoiner',
    description="%(prog)s merge multiple images into one image.",
    formatter_class=SingleMetavarHelpFormatter)
parser.add_argument('-w', '--width',
    type=int,
    default=640,
    help="The image width of the output image")
parser.add_argument('-f', '--format',
    type=str,
    choices=["jpg", "jpeg", "png"],
    default="png",
    metavar="FORMAT",
    help="The format of the output image")
parser.add_argument('-tb', '--top-border',
    type=int,
    default=0,
    metavar='TOP BORDER',
    dest='top',
    help="The top border of each image")
parser.add_argument('-bb', '--bottom-border',
    type=int,
    default=0,
    metavar='BOTTOM BORDER',
    dest='bottom',
    help="The bottom border of each image")
parser.add_argument('-c', '--border-color',
    type=int,
    default=0x000000,
    metavar='BORDER COLOR',
    dest='border_color',
    help="The border color between images(hexadecimal)")
parser.add_argument('-t', '--type',
    type=str,
    choices=['subtitle', 'image'],
    default=0,
    required=True,
    help="The type of the merge action. 'subtitle' only keeps subtitle except the first image. 'image' keeps all images")
parser.add_argument('-s', '--subtitle-height',
    type=int,
    default=120,
    metavar='SUBTITLE HEIGHT',
    dest='subtitle_height',
    required=True,
    help="The distance between the top of the subtitle and the bottom of the image.")
parser.add_argument('files',
    type=str,
    nargs='+',
    help="The image files")
parser.add_argument('-v', '--version',
    action='version',
    version='%(prog)s 0.1')

args = parser.parse_args()
print args

width = args.width
format = args.format
print width
print format

for f in args.files:
    print f

# 1600*900
height = int(round(900 * (640 * 1.0 / 1600)))
print height
