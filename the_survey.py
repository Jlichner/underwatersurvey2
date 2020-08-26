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
    total_surveyed,
    )
from data import (
    AngleIronToIslanderGap,
    BarToPlatform,
    BobsArrowToEmmaMunsen,
    BobsArrowToIslander,
    BypassEndToBobsArrow,
    CarToLisasGift,
    FourWayToBypassEndSixtyFoot,
    FourWayToNatesTieoff,
    IslanderGapToFourWay,
    JJJ,
    KibbettsToWreck2,
    Landmark,
    LisasGiftNortheast,
    LisasGiftToKibbetts,
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
)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

matplotlib.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots()
fig.set_size_inches(18, 12)
ax.set_aspect(aspect='equal')

FONTSIZE=24
LANDMARK_ZOOM=40
LEGEND_IMAGE_STRETCH=(-14, 7)
LEGEND_IMAGE_OFFSET=(-8, 5)

draw_kwargs = {
    'depth_distance': 10,
    'depth_fontsize': 10,
    'draw_mooringblocks': True,
    'draw_tieoffs': True,
    'landmark_markersize': 8,
    'landmark_zoom': LANDMARK_ZOOM,
    'text_fontsize': 8,
    'tieoff_size': 3,
}


######
#
# Draw the recreational area, forcing both the right loop and the left loop to close up
#
#####

draw(ax, Landmark.BAR, BarToPlatform, **draw_kwargs)

draw_circuit(ax, Landmark.SKELETON, SkeletonToMooringBlock2ViaPokerRun, SkeletonToMooringBlock2ViaMooringBlocks, **draw_kwargs)

draw(ax, Landmark.MOORING_BLOCK_2, MooringBlock2ToMooringBlock1, **draw_kwargs)

draw_circuit(ax, Landmark.MOORING_BLOCK_1, MooringBlock1ToMooringBlock5ViaPokerRun, MooringBlock1ToMooringBlock5ViaMooringBlocks, **draw_kwargs)

draw(ax, Landmark.UMBRELLA, UmbrellaToOxygenTanks, **draw_kwargs)

draw(ax, Landmark.CAR, CarToLisasGift, **draw_kwargs)

######
#
# Draw upstream of the recreation area
#
######


draw(ax, Landmark.UMBRELLA, UmbrellaToRockIsland, **draw_kwargs)

draw(ax, Landmark.ROCK_ISLAND_BOTTLE, RockIslandBottleCounterClockwise, **draw_kwargs)

draw(ax, Landmark.ANGLE_IRON, AngleIronToIslanderGap, **draw_kwargs)

draw(ax, Landmark.ISLANDER_GAP, IslanderGapToFourWay, **draw_kwargs)

draw(ax, Landmark.FOUR_WAY, FourWayToNatesTieoff, **draw_kwargs)

draw_circuit(ax, Landmark.FOUR_WAY, FourWayToBypassEndSixtyFoot, JJJ, **draw_kwargs)

draw(ax, Landmark.BYPASS_END_JJJ, BypassEndToBobsArrow, **draw_kwargs)

draw(ax, Landmark.BOBS_ARROW, BobsArrowToIslander, **draw_kwargs)

draw(ax, Landmark.BOBS_ARROW, BobsArrowToEmmaMunsen, **draw_kwargs)

draw(ax, Landmark.ROCK_ISLAND_BOTTLE, RockIslandBottleClockwise, **draw_kwargs)

######
#
# Draw more of the map, forcing the box to be a closed
#
######

draw_between_landmarks(ax, Landmark.NATES_TIEOFF, Landmark.ROCK_ISLAND_T, NatesTieoffToRockIsland, **draw_kwargs)

draw(ax, Landmark.ROCK_ISLAND_T, RockIslandTClockwise, **draw_kwargs)

#####
#
# Draw downstream ofthe recreational area
#
#####

draw(ax, Landmark.LISAS_GIFT, LisasGiftToKibbetts, **draw_kwargs)

draw(ax, Landmark.KIBBETTS, KibbettsToWreck2, **draw_kwargs)

draw(ax, Landmark.LISAS_GIFT, LisasGiftNortheast, **draw_kwargs)

#####
#
# Center the map
#
#####

((x_min, y_min), (x_max, y_max)) = corner_coordinates()
y_max = y_max + 200
y_min = y_min - 350
x_avg = (x_min + x_max) / 2
x_min = x_avg - 3 * (y_max - y_min) / 4
x_max = x_avg + 3 * (y_max - y_min) / 4

plt.axis('off')
plt.title('BONNIE CASTLE SCUBA PARK', fontname ='Helvetica', fontsize=3.5 * FONTSIZE, fontweight='bold')
plt.text(x=(x_min + x_max)/2, y=y_max, s='A project of Bonnie Castle Resort, All About Scuba, Blue Foot Diving, and Northeast Underwater Explorers', fontname ='Helvetica', fontsize=1.1 * FONTSIZE, fontweight='bold', ha='center', va='top')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#####
#
# Add a compass rose, distance marker, and copyright statement
#
#####

# draw_compass_rose()
draw_scale(x_min, y_min, distance=150, depth=30, text_distance=30, fontsize=0.8 * FONTSIZE, feet=(0, 250, 500, 750, 1000), meters=(0, 100, 200, 300))
draw_platforms()
draw_boat_ramp()
# add_copyright(fontsize=0.78 * FONTSIZE)

#####
#
# Create the legend
# TODO(stpyang): put this in a different file
#
#####

ARROW = Line2D([0], [0], label='Arrow', color='black', linewidth=0, marker='^', markersize=7, markerfacecolor='white')
TIE_OFF = Line2D([0], [0], label='Tie off', color='blue', linewidth=0, marker='h', markersize=5)
STAKE = Line2D([0], [0], label='Stake', color='brown', linewidth=0, marker='s', markersize=5)
SURVEYED_LINE = Line2D([0], [0], label='Surveyed line', color='black', linestyle='solid', linewidth=2)
UNSURVEYED_LINE = Line2D([0], [0], label='Unsurveyed line', color='black', linestyle='dotted', linewidth=2)
REMOVED_LINE = Line2D([0], [0], label='Removed line', color='lightgrey', linestyle='solid')
MARINA_LINE = Line2D([0], [0], label='CAUTION: Boat traffic overhead', color='red', linestyle='solid')

ANCHOR = Line2D([0], [0], label='Anchor')
CAR = Line2D([0], [0], label='Car')
CONROY = Line2D([0], [0], label='Conroy')
EMMA_MUNSEN_TUGBOAT = Line2D([0], [0], label='Emma Munsen tugboat')
GIFT = Line2D([0], [0], label='Lisa\'s Gift')
MOORING_BLOCK = Line2D([0], [0], label='Mooring block')
NATES_TIEOFF = Line2D([0], [0], label='Nate\'s fugly tieoff')
OXYGEN = Line2D([0], [0], label='Oxygen bottles')
SHIPWRECK = Line2D([0], [0], label='Shipwreck')
SKELETON = Line2D([0], [0], label='Skeleton')
TRACTOR_TIRE = Line2D([0], [0], label='Big tire')
UMBRELLA = Line2D([0], [0], label='Umbrella')
WHEEL = Line2D([0], [0], label='Wagon wheels')

anchor_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png')
car_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png')
conroy_handler = ImageHandler(image_path='icons/conroy.png')
emma_munsen_tugboat_handler = ImageHandler(image_path='icons/tugboat.png')
gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png')
mooring_block_handler = ImageHandler(image_path='icons/mooringblock.png', image_stretch=(-10, 2), image_offset=(-5, 1))
nates_tieoff_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-233-lasso@3x.png')
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png')
shipwreck_handler = ImageHandler(image_path='icons/shipwreck.png')
skeleton_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png')
tractor_tire_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-137-cogwheel@3x.png')
umbrella_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png')
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png')

# ax.legend(
#     handles=[
#         ANCHOR,
#         ARROW,
#         CAR,
#         CONROY,
#         EMMA_MUNSEN_TUGBOAT,
#         GIFT,
#         MARINA_LINE,
#         MOORING_BLOCK,
#         NATES_TIEOFF,
#         OXYGEN,
#         SHIPWRECK,
#         SKELETON,
#         STAKE,
#         SURVEYED_LINE,
#         TIE_OFF,
#         TRACTOR_TIRE,
#         UMBRELLA,
#         UNSURVEYED_LINE,
#         WHEEL,
#         ],
#     handler_map={
#         ANCHOR: anchor_handler,
#         CAR: car_handler,
#         CONROY: conroy_handler,
#         EMMA_MUNSEN_TUGBOAT: emma_munsen_tugboat_handler,
#         GIFT: gift_handler,
#         MOORING_BLOCK: mooring_block_handler,
#         NATES_TIEOFF: nates_tieoff_handler,
#         OXYGEN: oxygen_handler,
#         SHIPWRECK: shipwreck_handler,
#         SKELETON: skeleton_handler,
#         TRACTOR_TIRE: tractor_tire_handler,
#         UMBRELLA: umbrella_handler,
#         WHEEL: wheel_handler,
#         },
    # fontsize=0.9 * FONTSIZE,
    # labelspacing=0.6,
#     loc='lower right')

print('{} total line surveyed'.format(total_surveyed()))

plt.savefig('maps/the_survey.png', transparent=True)
