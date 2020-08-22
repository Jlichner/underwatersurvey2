from base import (
    add_copyright,
    corner_coordinates,
    draw,
    draw_between_landmarks,
    draw_boat_ramp,
    draw_circuit,
    draw_compass_rose,
    draw_platforms,
    draw_scale,
    get_landmark_coordinates,
    ImageHandler,
    )
from data import (
    AngleIronToFourWay,
    BarToPlatform,
    BobsArrowToEmmaMunsen,
    BobsArrowToIslander,
    BypassEndToBobsArrow,
    CarToLisasGift,
    FourWayToBypassEndSixtyFoot,
    FourWayToNatesTieoff,
    JJJ,
    Landmark,
    LisasGiftNortheast,
    LisasGiftToWreck1,
    MooringBlock1ToMooringBlock5ViaMooringBlocks,
    MooringBlock1ToMooringBlock5ViaPokerRun,
    MooringBlock2ToMooringBlock1,
    NatesTieoffToRockIsland,
    RockIslandBottleClockwise,
    RockIslandBottleCounterClockwise,
    RockIslandTClockwise,
    SkeletonToMooringBlock2ViaMooringBlocks,
    SkeletonToMooringBlock2ViaPokerRun,
    UmbrellaToOxygenTanks,
    UmbrellaToRockIsland,
    Wreck1ToWreck2,
)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

matplotlib.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots()
fig.set_size_inches(18, 12)
ax.set_aspect(aspect='equal')

######
#
# Draw the recreational area, forcing both the right loop and the left loop to close up
#
#####

draw(ax, Landmark.BAR, BarToPlatform, recreational=True)

draw_circuit(ax, Landmark.SKELETON, SkeletonToMooringBlock2ViaPokerRun, SkeletonToMooringBlock2ViaMooringBlocks, recreational=True)

draw(ax, Landmark.MOORING_BLOCK_2, MooringBlock2ToMooringBlock1, recreational=True)

draw_circuit(ax, Landmark.MOORING_BLOCK_1, MooringBlock1ToMooringBlock5ViaPokerRun, MooringBlock1ToMooringBlock5ViaMooringBlocks, recreational=True)

draw(ax, Landmark.UMBRELLA, UmbrellaToOxygenTanks, recreational=True)

draw(ax, Landmark.CAR, CarToLisasGift, recreational=True)

#####
#
# Center the map
#
#####

plt.axis('off')
plt.title('Bonnie Castle Scuba Park\n', fontsize=18)
((x_min, y_min), (x_max, y_max)) = corner_coordinates()
plt.xlim(x_min - 50, x_max + 50)
plt.ylim(y_min - 50, y_max + 50)

#####
#
# Add a compass rose, distance marker, and copyright statement
#
#####

draw_compass_rose(recreational=True)
draw_scale(recreational=True)
draw_platforms()
draw_boat_ramp()
add_copyright()

#####
#
# Create the legend
# TODO(stpyang): put this in a different file
#
#####

ARROW = Line2D([0], [0], label='Arrow', color='black', linewidth=0, marker='^', markersize=5, markerfacecolor='white')
TIE_OFF = Line2D([0], [0], label='Tie off', color='blue', linewidth=0, marker='h', markersize=5)
STAKE = Line2D([0], [0], label='Stake', color='brown', linewidth=0, marker='s', markersize=5)
SURVEYED_LINE = Line2D([0], [0], label='Surveyed line', color='black', linestyle='solid', linewidth=2)
UNSURVEYED_LINE = Line2D([0], [0], label='Unsurveyed line', color='black', linestyle='dotted', linewidth=2)
# REMOVED_LINE = Line2D([0], [0], label='Removed line', color='lightgrey', linestyle='solid')
MARINA_LINE = Line2D([0], [0], label='CAUTION: Boat traffic overhead', color='red', linestyle='solid')

ANCHOR = Line2D([0], [0], label='Anchor')
CAR = Line2D([0], [0], label='Car')
CONROY = Line2D([0], [0], label='Conroy')
GIFT = Line2D([0], [0], label='Lisa\'s Gift')
MOORING_BLOCK = Line2D([0], [0], label='Mooring block')
OXYGEN = Line2D([0], [0], label='Oxygen bottles')
SKELETON = Line2D([0], [0], label='Skeleton')
UMBRELLA = Line2D([0], [0], label='Umbrella')
WHEEL = Line2D([0], [0], label='Wagon wheels')

anchor_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png')
car_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png')
conroy_handler = ImageHandler(image_path='icons/conroy.png')
gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png')
mooring_block_handler = ImageHandler(image_path='icons/mooringblock.png', image_stretch=(-10, 2), image_offset=(-5, 1))
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png')
skeleton_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png')
umbrella_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png')
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png')

ax.legend(
    handles=[
        ARROW,
        TIE_OFF,
        STAKE,
        SURVEYED_LINE,
        UNSURVEYED_LINE,
        MARINA_LINE,

        ANCHOR,
        CAR,
        CONROY,
        GIFT,
        MOORING_BLOCK,
        OXYGEN,
        SKELETON,
        UMBRELLA,
        WHEEL,
    ],
    handler_map={
        ANCHOR: anchor_handler,
        CAR: car_handler,
        CONROY: conroy_handler,
        GIFT: gift_handler,
        MOORING_BLOCK: mooring_block_handler,
        OXYGEN: oxygen_handler,
        SKELETON: skeleton_handler,
        UMBRELLA: umbrella_handler,
        WHEEL: wheel_handler,
        },
    fontsize=6,
    labelspacing=1.2,
    loc='lower right')

# plt.savefig('rec_survey.png', transparent=True)
plt.savefig('rec_survey.pdf')
