from base import (
    compass_rose,
    copyright,
    corner_coordinates,
    distance_ruler,
    draw,
    ImageHandler,
    straight_distance_angle,
    survey_distance_angle,
    )
from data import (
    BobsArrowToEmmaMunsen,
    BobsArrowToIslander,
    BypassEndToBobsArrow,
    CarToKibbetts,
    FourWayToBypassEndSixtyFoot,
    FourWayToNatesTieoff,
    JJJ,
    Landmark,
    NatesTieoffToRockIsland,
    PlatformToFourWay,
    PokerRun,
    RockIslandBottleClockwise,
    RockIslandBottleCounterClockwise,
    RockIslandTClockwise,
    UmbrellaToOxygenTanks,
    UmbrellaToRockIsland,
)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib._png import read_png
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.transforms import Bbox

matplotlib.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots()
fig.set_size_inches(36, 24)
ax.set_aspect(aspect='equal')

total_surveyed = 0

######
#
# Draw some of the map, forcing the bypass and the jjj line to intersect
#
######

(distance_jjj, angle_jjj) = survey_distance_angle(FourWayToBypassEndSixtyFoot)
(distance_sixty_foot, angle_sixty_foot) = survey_distance_angle(JJJ)
stretch_jjj = 2 * distance_jjj / (distance_jjj + distance_sixty_foot)
stretch_sixty_foot = 2 * distance_sixty_foot / (distance_jjj + distance_sixty_foot)
rotation_jjj = (angle_sixty_foot - angle_jjj) / 2
rotation_sixty_foot = (angle_jjj - angle_sixty_foot) / 2

total_surveyed = draw(ax, total_surveyed, Landmark.MOORING_BLOCK, PokerRun)

total_surveyed = draw(ax, total_surveyed, Landmark.CAR, CarToKibbetts)

total_surveyed = draw(ax, total_surveyed, Landmark.UMBRELLA, UmbrellaToOxygenTanks)

total_surveyed = draw(ax, total_surveyed, Landmark.UMBRELLA, UmbrellaToRockIsland)

total_surveyed = draw(ax, total_surveyed, Landmark.ROCK_ISLAND_BOTTLE, RockIslandBottleCounterClockwise)

total_surveyed = draw(ax, total_surveyed, Landmark.PLATFORM_SW, PlatformToFourWay)

total_surveyed = draw(ax, total_surveyed, Landmark.FOUR_WAY, FourWayToNatesTieoff)

total_surveyed = draw(ax, total_surveyed, Landmark.FOUR_WAY, FourWayToBypassEndSixtyFoot, stretch=stretch_sixty_foot, rotation=rotation_sixty_foot)

total_surveyed = draw(ax, total_surveyed, Landmark.FOUR_WAY, JJJ, stretch=stretch_jjj, rotation=rotation_jjj)

total_surveyed = draw(ax, total_surveyed, Landmark.BYPASS_END_JJJ, BypassEndToBobsArrow)

total_surveyed = draw(ax, total_surveyed, Landmark.BOBS_ARROW, BobsArrowToIslander)

total_surveyed = draw(ax, total_surveyed, Landmark.BOBS_ARROW, BobsArrowToEmmaMunsen)

total_surveyed = draw(ax, total_surveyed, Landmark.ROCK_ISLAND_BOTTLE, RockIslandBottleClockwise)

######
#
# Draw more of the map, forcing the box to be a closed
#
######

(distance_rock, angle_rock) = straight_distance_angle(Landmark.NATES_TIEOFF, Landmark.ROCK_ISLAND_T)
(distance_nate, angle_nate) = survey_distance_angle(NatesTieoffToRockIsland)
stretch_nate = distance_rock / distance_nate
rotation_nate = angle_nate - angle_rock

total_surveyed = draw(ax, total_surveyed, Landmark.NATES_TIEOFF, NatesTieoffToRockIsland, stretch=stretch_nate, rotation=rotation_nate)

total_surveyed = draw(ax, total_surveyed, Landmark.ROCK_ISLAND_T, RockIslandTClockwise)

#####
#
# Center the map
#
#####

plt.axis('off')
plt.title('Bonnie Castle Scuba Park\n', fontsize=36)
((x_min, y_min), (x_max, y_max)) = corner_coordinates()
plt.xlim(x_min - 50, x_max + 50)
plt.ylim(y_min - 50, y_max + 50)

#####
#
# Add a compass rose, distance marker, and copyright statement
#
#####

compass_rose(ax)
distance_ruler(ax)
copyright(ax)

#####
#
# Create the legend
# TODO(stpyang): put this in a different file
#
#####

ARROW = Line2D([0], [0], label='Arrow', color='black', linewidth=0, marker='^', markersize=7, markerfacecolor='white')
# PLATFORM = Patch(label='Platform', facecolor='darkgoldenrod')
TIE_OFF = Line2D([0], [0], label='Tie off', color='blue', linewidth=0, marker='h', markersize=5)
STAKE = Line2D([0], [0], label='Stake', color='brown', linewidth=0, marker='s', markersize=5)
SURVEYED_LINE = Line2D([0], [0], label='Surveyed line', color='black', linestyle='solid', linewidth=2)
UNSURVEYED_LINE = Line2D([0], [0], label='Unsurveyed line', color='black', linestyle='dotted', linewidth=2)
REMOVED_LINE = Line2D([0], [0], label='Removed line', color='lightgrey', linestyle='solid')
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
NATES_TIEOFF = Line2D([0], [0], label='Nate\'s fugly tieoff')
EMMA_MUNSEN_TUGBOAT = Line2D([0], [0], label='Emma Munsen tugboat')

skeleton_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
car_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
umbrella_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
anchor_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
rowboat_handler = ImageHandler(image_path='icons/rowboat.png', image_stretch=(11, 26), image_offset=(6, 12))
conroy_handler = ImageHandler(image_path='icons/conroy.png', image_stretch=(0, 16), image_offset=(0, 8))
nates_tieoff_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-233-lasso@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
emma_munsen_tugboat_handler = ImageHandler(image_path='icons/tugboat.png', image_stretch=(6, 14), image_offset=(4, 8))

ax.legend(
    handles=[SURVEYED_LINE, UNSURVEYED_LINE, MARINA_LINE, STAKE, TIE_OFF, ARROW, SKELETON, CAR, UMBRELLA, ANCHOR, WHEEL, GIFT, ROWBOAT, OXYGEN, CONROY, NATES_TIEOFF, EMMA_MUNSEN_TUGBOAT],
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
        NATES_TIEOFF: nates_tieoff_handler,
        EMMA_MUNSEN_TUGBOAT: emma_munsen_tugboat_handler,
        },
    fontsize=10,
    labelspacing=1.2,
    loc='lower right')

print('{} total line surveyed'.format(total_surveyed))

plt.savefig('survey.pdf')
