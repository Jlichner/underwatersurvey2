from base import (
    corner_coordinates,
    draw,
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
    AnchorToSailboatTruncated,
    AngleIronToMaryTruncated,
    BarToPlatform,
    CarToLisasGiftTruncated,
    ConroyToOxygenTanksTruncated,
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

FONTSIZE=60
LANDMARK_ZOOM=80
LEGEND_IMAGE_STRETCH=(-17, 7.5)
LEGEND_IMAGE_OFFSET=(-8, 4)

draw_kwargs = {
    'depth_distance': 0.27 * FONTSIZE,
    'depth_fontsize': 0.25 * FONTSIZE,
    'draw_tieoffs': False,
    'include_depth': True,
    'include_mooringblocks': True,
    'include_text': True,
    'landmark_markersize': 16,
    'landmark_zoom': LANDMARK_ZOOM,
    'linewidth': 1,
    'text_fontsize': 13,
    'tieoff_size': 6,
}

######
#
# Draw the recreational area, forcing both the right loop and the left loop to close up
#
#####

draw(ax, Landmark.BAR, BarToPlatform, **draw_kwargs)

draw_circuit(ax, Landmark.SKELETON, SkeletonToMooringBlock2ViaPokerRun, SkeletonToMooringBlock2ViaMooringBlocks, **draw_kwargs)

draw(ax, Landmark.ANCHOR, AnchorToSailboatTruncated, **draw_kwargs)

draw(ax, Landmark.MOORING_BLOCK_2, MooringBlock2ToMooringBlock1, **draw_kwargs)

draw_circuit(ax, Landmark.MOORING_BLOCK_1, MooringBlock1ToMooringBlock5ViaPokerRun, MooringBlock1ToMooringBlock5ViaMooringBlocks, **draw_kwargs)

draw(ax, Landmark.UMBRELLA, UmbrellaToOxygenTanksTruncated, **draw_kwargs)

draw(ax, Landmark.CONROY, ConroyToOxygenTanksTruncated, **draw_kwargs)

draw(ax, Landmark.CAR, CarToLisasGiftTruncated, **draw_kwargs)

draw(ax, Landmark.ANGLE_IRON, AngleIronToMaryTruncated, **draw_kwargs)

#####
#
# Add the skeleton
#
#####

(x, y) = get_landmark_coordinates()[Landmark.SKELETON]
draw_skeleton(ax, x + 3, y + 9, depth=64, depth_angle=70, depth_distance=0.21 * FONTSIZE, depth_fontsize=0.25 * FONTSIZE, landmark_zoom=LANDMARK_ZOOM)

#####
#
# Center the map
#
#####

((x_min, y_min), (x_max, y_max)) = corner_coordinates()
y_min = y_min - 75
y_max = y_max + 50
x_avg = (x_min + x_max) / 2
x_min = x_avg - 5 * (y_max - y_min) / 6
x_max = x_avg + 5 * (y_max - y_min) / 6

plt.axis('off')
plt.title('BONNIE CASTLE SCUBA PARK', fontname ='Helvetica Neue', fontsize=FONTSIZE, fontweight='bold')
plt.text(x=(x_min + x_max) / 2, y=(0.99 * y_max + 0.01 * y_min), s='A project of Bonnie Castle Resort, All About Scuba, Blue Foot Diving, and Northeast Underwater Explorers', fontname ='Helvetica', fontsize=0.318 * FONTSIZE, ha='center', va='top')
plt.text(x=x_min, y=(- 0.05 * y_max + 1.05 * y_min), s='© 2021 NORTHEAST UNDERWATER EXPLORERS', fontname ='Helvetica', fontsize=0.22 * FONTSIZE, ha='left', va='top')
plt.text(x=x_max, y=(- 0.05 * y_max + 1.05 * y_min), s='v1.1 September 2021', fontname ='Helvetica', fontsize=0.22 * FONTSIZE, ha='right', va='top')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#####
#
# Add a compass rose, distance marker, and copyright statement
#
#####

draw_platforms(fontsize=0.20 * FONTSIZE)
draw_boat_ramp()
draw_scale(corner_coordinates=((x_min, y_min), (x_max, y_max)), fontsize=0.25 * FONTSIZE, feet=(0, 50, 100, 150), meters=(0, 10, 20, 30, 40, 50))
draw_compass_rose(ax, corner_coordinates=((x_min, y_min), (x_max, y_max)), zoom=0.1)


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

legend = ax.legend(
    edgecolor='black',
    fontsize=0.30 * FONTSIZE,
    framealpha=0.0,
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
    labelspacing=0.6,
    loc='lower right',
)

plt.savefig('maps/rec_survey_1.png', transparent=True)
