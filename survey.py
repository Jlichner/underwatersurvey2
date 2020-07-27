from base import (
    add_copyright,
    corner_coordinates,
    draw,
    draw_circuit,
    draw_compass_rose,
    draw_platforms,
    draw_scale,
    draw_boat_ramp,
    get_landmark_coordinates,
    ImageHandler,
    straight_distance_angle,
    survey_distance_angle,
    total_surveyed
    )
from data import (
    BarToPlatform,
    BobsArrowToEmmaMunsen,
    BobsArrowToIslander,
    BypassEndToBobsArrow,
    CarToLisasGift,
    FourWayToBypassEndSixtyFoot,
    FourWayToNatesTieoff,
    JJJ,
    Landmark,
    LisasGiftToWreck1,
    LisasGiftNortheast,
    NatesTieoffToRockIsland,
    MooringBlock2ToMooringBlock1,
    MooringBlock1ToMooringBlock5ViaMooringBlocks,
    MooringBlock1ToMooringBlock5ViaPokerRun,
    AngleIronToFourWay,
    RockIslandBottleClockwise,
    RockIslandBottleCounterClockwise,
    RockIslandTClockwise,
    SkeletonToMooringBlock2ViaPokerRun,
    SkeletonToMooringBlock2ViaMooringBlocks,
    UmbrellaToOxygenTanks,
    UmbrellaToRockIsland,
    Wreck1ToWreck2,
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

######
#
# Draw the recreational area, forcing both the right loop and the left loop to close up
#
#####

draw(ax, Landmark.BAR, BarToPlatform)

draw_circuit(ax, Landmark.SKELETON, SkeletonToMooringBlock2ViaPokerRun, SkeletonToMooringBlock2ViaMooringBlocks)

draw(ax, Landmark.MOORING_BLOCK_2, MooringBlock2ToMooringBlock1)

draw_circuit(ax, Landmark.MOORING_BLOCK_1, MooringBlock1ToMooringBlock5ViaPokerRun, MooringBlock1ToMooringBlock5ViaMooringBlocks)

######
#
# Draw upstream of the recreation area
#
######

draw(ax, Landmark.UMBRELLA, UmbrellaToOxygenTanks)

draw(ax, Landmark.UMBRELLA, UmbrellaToRockIsland)

draw(ax, Landmark.ROCK_ISLAND_BOTTLE, RockIslandBottleCounterClockwise)

draw(ax, Landmark.ANGLE_IRON, AngleIronToFourWay)

draw(ax, Landmark.FOUR_WAY, FourWayToNatesTieoff)

draw_circuit(ax, Landmark.FOUR_WAY, FourWayToBypassEndSixtyFoot, JJJ)

draw(ax, Landmark.BYPASS_END_JJJ, BypassEndToBobsArrow)

draw(ax, Landmark.BOBS_ARROW, BobsArrowToIslander)

draw(ax, Landmark.BOBS_ARROW, BobsArrowToEmmaMunsen)

draw(ax, Landmark.ROCK_ISLAND_BOTTLE, RockIslandBottleClockwise)

######
#
# Draw more of the map, forcing the box to be a closed
#
######

(distance_rock, angle_rock) = straight_distance_angle(Landmark.NATES_TIEOFF, Landmark.ROCK_ISLAND_T)
(distance_nate, angle_nate) = survey_distance_angle(NatesTieoffToRockIsland)
stretch_nate = distance_rock / distance_nate
rotation_nate = angle_nate - angle_rock

draw(ax, Landmark.NATES_TIEOFF, NatesTieoffToRockIsland, stretch=stretch_nate, rotation=rotation_nate)

draw(ax, Landmark.ROCK_ISLAND_T, RockIslandTClockwise)

#####
#
# Draw downstream ofthe recreational area
#
#####

draw(ax, Landmark.CAR, CarToLisasGift)
draw(ax, Landmark.LISAS_GIFT, LisasGiftToWreck1)
draw(ax, Landmark.WRECK_1, Wreck1ToWreck2)
draw(ax, Landmark.LISAS_GIFT, LisasGiftNortheast)

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

draw_compass_rose()
draw_scale()
draw_platforms()
draw_boat_ramp()
add_copyright()

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
SHIPWRECK = Line2D([0], [0], label='Shipwreck')
OXYGEN = Line2D([0], [0], label='Oxygen bottles')
CONROY = Line2D([0], [0], label='Conroy')
NATES_TIEOFF = Line2D([0], [0], label='Nate\'s fugly tieoff')
EMMA_MUNSEN_TUGBOAT = Line2D([0], [0], label='Emma Munsen tugboat')
MOORING_BLOCK = Line2D([0], [0], label='Mooring block')

skeleton_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png')
car_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png')
umbrella_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png')
anchor_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png')
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png')
gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png')
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png')
mooring_block_handler = ImageHandler(image_path='icons/mooringblock.png', image_stretch=(-10, 2), image_offset=(-5, 1))
shipwreck_handler = ImageHandler(image_path='icons/shipwreck.png')
conroy_handler = ImageHandler(image_path='icons/conroy.png')
nates_tieoff_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-233-lasso@3x.png')
emma_munsen_tugboat_handler = ImageHandler(image_path='icons/tugboat.png')

ax.legend(
    handles=[SURVEYED_LINE, UNSURVEYED_LINE, MARINA_LINE, STAKE, TIE_OFF, MOORING_BLOCK, ARROW, SKELETON, CAR, UMBRELLA, ANCHOR, WHEEL, GIFT, SHIPWRECK, OXYGEN, CONROY, NATES_TIEOFF, EMMA_MUNSEN_TUGBOAT],
    handler_map={
        ANCHOR: anchor_handler,
        CAR: car_handler,
        CONROY: conroy_handler,
        EMMA_MUNSEN_TUGBOAT: emma_munsen_tugboat_handler,
        GIFT: gift_handler,
        MOORING_BLOCK: mooring_block_handler,
        NATES_TIEOFF: nates_tieoff_handler,
        OXYGEN: oxygen_handler,
        SHIPWRECK: shipwreck_handler,
        SKELETON: skeleton_handler,
        UMBRELLA: umbrella_handler,
        WHEEL: wheel_handler,
        },
    fontsize=10,
    labelspacing=1.2,
    loc='lower right')

print('{} total line surveyed'.format(total_surveyed()))

# plt.savefig('survey.png', transparent=True)
plt.savefig('survey.pdf')
