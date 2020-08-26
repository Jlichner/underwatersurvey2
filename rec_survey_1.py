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
    AngleIronToIslanderGapTruncated,
    BarToPlatform,
    CarToLisasGiftTruncated,
    Landmark,
    MooringBlock1ToMooringBlock5ViaMooringBlocks,
    MooringBlock1ToMooringBlock5ViaPokerRun,
    MooringBlock2ToMooringBlock1,
    SkeletonToMooringBlock2ViaMooringBlocks,
    SkeletonToMooringBlock2ViaPokerRun,
    UmbrellaToOxygenTanksTruncated,
)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

matplotlib.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots()
fig.set_size_inches(18, 12)
ax.set_aspect(aspect='equal')

FONTSIZE=24
LANDMARK_ZOOM=80
LEGEND_IMAGE_STRETCH=(-17, 11)
LEGEND_IMAGE_OFFSET=(-8, 5)

draw_kwargs = {
    'depth_distance': 10,
    'depth_fontsize': 10,
    'draw_mooringblocks': True,
    'draw_tieoffs': False,
    'landmark_markersize': 16,
    'landmark_zoom': LANDMARK_ZOOM,
    'text_fontsize': 15,
    'tieoff_size': 6,
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

draw(ax, Landmark.UMBRELLA, UmbrellaToOxygenTanksTruncated, **draw_kwargs)

draw(ax, Landmark.CAR, CarToLisasGiftTruncated, **draw_kwargs)

draw(ax, Landmark.ANGLE_IRON, AngleIronToIslanderGapTruncated, **draw_kwargs)

#####
#
# Add the skeleton
#
#####

(x, y) = get_landmark_coordinates()[Landmark.SKELETON]
draw_skeleton(ax, x + 3, y + 9, landmark_zoom=LANDMARK_ZOOM)

#####
#
# Center the map
#
#####

((x_min, y_min), (x_max, y_max)) = corner_coordinates()
y_min = y_min - 50
y_max = y_max + 50
x_avg = (x_min + x_max) / 2
x_min = x_avg - 3 * (y_max - y_min) / 4
x_max = x_avg + 3 * (y_max - y_min) / 4

plt.axis('off')
plt.title('BONNIE CASTLE SCUBA PARK', fontname ='Helvetica', fontsize=3.5 * FONTSIZE, fontweight='bold')
plt.text(x=(x_min + x_max)/2, y=y_max, s='A project of Bonnie Castle Resort, All About Scuba, Blue Foot Diving, and Northeast Underwater Explorers', fontname ='Helvetica', fontsize=1.1* FONTSIZE, fontweight='bold', ha='center', va='top')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#####
#
# Add a compass rose, distance marker, and copyright statement
#
#####

draw_scale(x_min, y_min, distance=24, depth=5, text_distance=5, fontsize=0.8 * FONTSIZE, feet=(0, 50, 100, 150), meters=(0, 10, 20, 30, 40, 50))
draw_platforms()
draw_boat_ramp()
# add_copyright(fontsize=0.78 * FONTSIZE)

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
UMBRELLA = Line2D([0], [0], label='Umbrella')

anchor_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
car_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
conroy_handler = ImageHandler(image_path='icons/conroy.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
skeleton_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
umbrella_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)

ax.legend(
    handles=[
        MARINA_LINE,

        ANCHOR,
        CAR,
        CONROY,
        SKELETON,
        UMBRELLA,
    ],
    handler_map={
        ANCHOR: anchor_handler,
        CAR: car_handler,
        CONROY: conroy_handler,
        SKELETON: skeleton_handler,
        UMBRELLA: umbrella_handler,
        },
    fontsize=0.9 * FONTSIZE,
    labelspacing=0.6,
    loc='lower right')

plt.savefig('maps/rec_survey_1.png', transparent=True)
