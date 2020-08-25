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
    draw_skeleton,
    get_landmark_coordinates,
    ImageHandler,
    )
from data import (
    BarToPlatform,
    CarToLisasGift,
    Landmark,
    MooringBlock1ToMooringBlock5ViaMooringBlocks,
    MooringBlock1ToMooringBlock5ViaPokerRun,
    MooringBlock2ToMooringBlock1,
    SkeletonToMooringBlock2ViaMooringBlocks,
    SkeletonToMooringBlock2ViaPokerRun,
    UmbrellaToOxygenTanks,
)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

matplotlib.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots()
fig.set_size_inches(18, 12)
ax.set_aspect(aspect='equal')

FONTSIZE=20
LANDMARK_ZOOM=80
LANDMARK_MARKERSIZE=16
LEGEND_IMAGE_STRETCH=(-15, 11)
LEGEND_IMAGE_OFFSET=(-8, 5)
TIEOFF_SIZE=6

######
#
# Draw the recreational area, forcing both the right loop and the left loop to close up
#
#####

draw(ax, Landmark.BAR, BarToPlatform, draw_mooringblocks=False, draw_tieoffs=False, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw_circuit(ax, Landmark.SKELETON, SkeletonToMooringBlock2ViaPokerRun, SkeletonToMooringBlock2ViaMooringBlocks, draw_mooringblocks=False, draw_tieoffs=False, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw(ax, Landmark.MOORING_BLOCK_2, MooringBlock2ToMooringBlock1, draw_mooringblocks=False, draw_tieoffs=False, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw_circuit(ax, Landmark.MOORING_BLOCK_1, MooringBlock1ToMooringBlock5ViaPokerRun, MooringBlock1ToMooringBlock5ViaMooringBlocks, draw_mooringblocks=False, draw_tieoffs=False, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw(ax, Landmark.UMBRELLA, UmbrellaToOxygenTanks, draw_mooringblocks=False, draw_tieoffs=False, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw(ax, Landmark.CAR, CarToLisasGift, draw_mooringblocks=False, draw_tieoffs=False, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)


#####
#
# Add the skeleton
#
#####

# (x, y) = get_landmark_coordinates()[Landmark.SKELETON]
# draw_skeleton(ax, x + 3, y + 9, landmark_zoom=LANDMARK_ZOOM)

#####
#
# Center the map
#
#####

((x_min, y_min), (x_max, y_max)) = corner_coordinates()
x_min = x_min - 200
x_max = x_max + 200
y_min = y_min - 75

plt.axis('off')
plt.title('BONNIE CASTLE SCUBA PARK', fontname ='Helvetica', fontsize=3.0* FONTSIZE, fontweight='bold')
plt.text(x=(x_min + x_max)/2, y=(-0.055 * y_min + 1.055 * y_max), s='A project of Bonnie Castle Resort, All About Scuba, Blue Foot Diving, and Northeast Underwater Explorers', fontname ='Helvetica', fontsize=0.94 * FONTSIZE, fontweight='bold', ha='center')
plt.xlim(x_min - 50, x_max + 50)
plt.ylim(y_min - 50, y_max + 50)

#####
#
# Add a compass rose, distance marker, and copyright statement
#
#####

draw_scale(x_min, y_min - 30, distance=45, depth=10, text_distance=10, fontsize=FONTSIZE, feet=(0, 100, 200, 300), meters=(0, 20, 40, 60, 80))
draw_platforms()
draw_boat_ramp()
# add_copyright(fontsize=0.78 * FONTSIZE)

#####
#
# Create the legend
# TODO(stpyang): put this in a different file
#
#####

GIFT = Line2D([0], [0], label='Lisa\'s Gift')
OXYGEN = Line2D([0], [0], label='Oxygen bottles')
WHEEL = Line2D([0], [0], label='Wagon wheels')

gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)

ax.legend(
    handles=[
        GIFT,
        OXYGEN,
        WHEEL,
    ],
    handler_map={
        GIFT: gift_handler,
        OXYGEN: oxygen_handler,
        WHEEL: wheel_handler,
        },
    fontsize=FONTSIZE,
    labelspacing=0.8,
    loc='lower right')

plt.savefig('rec_survey_2.png', transparent=True)
# plt.savefig('rec_survey_2.pdf')
