from base import draw, ImageHandler
from data import Landmark, PokerRun, CarToKibbetts, PlatformToIslander, UmbrellaToRockIsland, UmbrellaToOxygenTanks, RockIslandTNorthwest, RockIslandTSoutheast, FourWayToRockIsland

import matplotlib
import matplotlib.pyplot as plt
from matplotlib._png import read_png
from matplotlib.lines import Line2D
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.patches import Patch
from matplotlib.transforms import Bbox

DRAW_DISTANCE = False

matplotlib.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots()
fig.set_size_inches(36, 24)
ax.set_aspect(aspect='equal')

total_surveyed = 0
corner_coordinates = ((0, 0), (0, 0))
landmark_coordinates = dict()
landmark_coordinates[Landmark.MOORING_BLOCK] = (0, 0)

(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, DRAW_DISTANCE, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.MOORING_BLOCK, PokerRun)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, DRAW_DISTANCE, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.CAR, CarToKibbetts)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, DRAW_DISTANCE, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.UMBRELLA, UmbrellaToOxygenTanks)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, DRAW_DISTANCE, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.UMBRELLA, UmbrellaToRockIsland)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, DRAW_DISTANCE, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.ROCK_ISLAND_T, RockIslandTNorthwest)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, DRAW_DISTANCE, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.ROCK_ISLAND_T, RockIslandTSoutheast)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, DRAW_DISTANCE, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.PLATFORM_SW, PlatformToIslander)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, DRAW_DISTANCE, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.FOUR_WAY, FourWayToRockIsland)

((x_min, y_min), (x_max, y_max)) = corner_coordinates
plt.axis('off')
plt.title('Bonnie Castle Scuba Park\n', fontsize=36)
plt.xlim(x_min - 50, x_max + 50)
plt.ylim(y_min - 50, y_max + 50)
ax.text(x_max, y_min - 100, 'Copyright 2020 NEUE.  All Rights Reserved.', fontsize=24, horizontalalignment='right')

#####
#
# Add compass rose
#
#####

im = OffsetImage(plt.imread('icons/compass.png'), zoom=35/ax.figure.dpi)
im.image.axes = ax
im_ab = AnnotationBbox(im, ((0.9 * x_min + 0.1 * x_max), (0.1 * y_min + 0.9 * y_max)), frameon=False)
ax.add_artist(im_ab)


#####
#
# Create the legend
#
#####

ARROW = Line2D([0], [0], label='Arrow', color='black', linewidth=0, marker='^', markersize=7, markerfacecolor='white')
# PLATFORM = Patch(label='Platform', facecolor='darkgoldenrod')
TIE_OFF = Line2D([0], [0], label='Tie Off', color='blue', linewidth=0, marker='h', markersize=5)
STAKE = Line2D([0], [0], label='Stake', color='brown', linewidth=0, marker='s', markersize=5)
SURVEYED_LINE = Line2D([0], [0], label='Surveyed Line', color='black', linestyle='solid', linewidth=2)
UNSURVEYED_LINE = Line2D([0], [0], label='Unsurveyed Line', color='black', linestyle='dotted', linewidth=2)
REMOVED_LINE = Line2D([0], [0], label='Removed Line', color='lightgrey', linestyle='solid')
MARINA_LINE = Line2D([0], [0], label='CAUTION: Boat traffic overhead', color='red', linestyle='solid')

SKELETON = Line2D([0], [0], label='Skeleton')
CAR = Line2D([0], [0], label='Car')
UMBRELLA = Line2D([0], [0], label='Umbrella')
ANCHOR = Line2D([0], [0], label='Anchor')
WHEEL = Line2D([0], [0], label='Wagon wheels')
GIFT = Line2D([0], [0], label='Lisa\'s Gift')
ROWBOAT = Line2D([0], [0], label='Rowboat')
OXYGEN = Line2D([0], [0], label='Oxygen bottles')
CONROY = Line2D([0], [0], label='Conroy')

skeleton_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
car_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
umbrella_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
anchor_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
rowboat_handler = ImageHandler(image_path='icons/rowboat.png', image_stretch=(11, 26), image_offset=(6, 12))
conroy_handler = ImageHandler(image_path='icons/conroy.png', image_stretch=(0, 16), image_offset=(0, 8))

ax.legend(
    handles=[SURVEYED_LINE, UNSURVEYED_LINE, MARINA_LINE, STAKE, TIE_OFF, ARROW, SKELETON, CAR, UMBRELLA, ANCHOR, WHEEL, GIFT, ROWBOAT, OXYGEN, CONROY],
    handler_map={
        SKELETON: skeleton_handler,
        CAR: car_handler,
        UMBRELLA: umbrella_handler,
        ANCHOR: anchor_handler,
        WHEEL: wheel_handler,
        GIFT: gift_handler,
        ROWBOAT: rowboat_handler,
        OXYGEN: oxygen_handler,
        CONROY: conroy_handler,
        },
    fontsize=10,
    labelspacing=1.2,
    loc='lower right')

print('{} total line surveyed'.format(total_surveyed))

plt.savefig('survey.pdf')
