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
LEGEND_IMAGE_STRETCH=(-15, 10)
LEGEND_IMAGE_OFFSET=(-8, 5)
TIEOFF_SIZE=6

######
#
# Draw the recreational area, forcing both the right loop and the left loop to close up
#
#####

FONTSIZE=10
LANDMARK_ZOOM=80
LANDMARK_MARKERSIZE=16
LEGEND_IMAGE_STRETCH=(-15, 10)
LEGEND_IMAGE_OFFSET=(-8, 5)
TIEOFF_SIZE=6

draw(ax, Landmark.BAR, BarToPlatform, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw_circuit(ax, Landmark.SKELETON, SkeletonToMooringBlock2ViaPokerRun, SkeletonToMooringBlock2ViaMooringBlocks, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw(ax, Landmark.MOORING_BLOCK_2, MooringBlock2ToMooringBlock1, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw_circuit(ax, Landmark.MOORING_BLOCK_1, MooringBlock1ToMooringBlock5ViaPokerRun, MooringBlock1ToMooringBlock5ViaMooringBlocks, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw(ax, Landmark.UMBRELLA, UmbrellaToOxygenTanks, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)

draw(ax, Landmark.CAR, CarToLisasGift, landmark_zoom=LANDMARK_ZOOM, landmark_markersize=LANDMARK_MARKERSIZE, tieoff_size=TIEOFF_SIZE)


#####
#
# Add the skeleton
#
#####

(x, y) = get_landmark_coordinates()[Landmark.SKELETON]
draw_skeleton(ax, x + 5, y + 11, landmark_zoom=2 * LANDMARK_ZOOM / 3)

#####
#
# Center the map
#
#####

plt.axis('off')
plt.title('Bonnie Castle Scuba Park\n', fontsize=2 * FONTSIZE)
((x_min, y_min), (x_max, y_max)) = corner_coordinates()
plt.xlim(x_min - 50, x_max + 50)
plt.ylim(y_min - 50, y_max + 50)

#####
#
# Add a compass rose, distance marker, and copyright statement
#
#####

draw_scale(x_min, y_max, text_distance=4, fontsize=FONTSIZE, feet=(0, 100, 200, 300), meters=(0, 25, 50, 100))
draw_platforms()
draw_boat_ramp()
add_copyright(fontsize=FONTSIZE)

#####
#
# Create the legend
# TODO(stpyang): put this in a different file
#
#####

MARINA_LINE = Line2D([0], [0], label='CAUTION: Traffic overhead', color='red', linestyle='solid')

ANCHOR = Line2D([0], [0], label='Anchor')
CAR = Line2D([0], [0], label='Car')
CONROY = Line2D([0], [0], label='Conroy')
SKELETON = Line2D([0], [0], label='Skeleton')

GIFT = Line2D([0], [0], label='Lisa\'s Gift')
OXYGEN = Line2D([0], [0], label='Oxygen bottles')
WHEEL = Line2D([0], [0], label='Wagon wheels')

anchor_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
car_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
conroy_handler = ImageHandler(image_path='icons/conroy.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
skeleton_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)

gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)

ax.legend(
    handles=[
        MARINA_LINE,

        ANCHOR,
        CAR,
        CONROY,
        SKELETON,

        GIFT,
        OXYGEN,
        WHEEL,
    ],
    handler_map={
        ANCHOR: anchor_handler,
        CAR: car_handler,
        CONROY: conroy_handler,
        SKELETON: skeleton_handler,

        GIFT: gift_handler,
        OXYGEN: oxygen_handler,
        WHEEL: wheel_handler,
        },
    fontsize=FONTSIZE,
    labelspacing=1.0,
    loc='lower right')

plt.savefig('rec_survey_big.png', transparent=True)
# plt.savefig('rec_survey_big.pdf')
