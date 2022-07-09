from base import (
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
    AnchorToSailboat,
    AngleIronToMary,
    BarToPlatform,
    CarToLisasGift,
    ConroyToOxygenTanks,
    Landmark,
    LisasGiftToKibbetts,
    MooringBlock1ToMooringBlock5ViaMooringBlocks,
    MooringBlock1ToMooringBlock5ViaPokerRun,
    MooringBlock2ToMooringBlock1,
    SkeletonToMooringBlock2ViaMooringBlocks,
    SkeletonToMooringBlock2ViaPokerRun,
    UmbrellaToOxygenTanks,
    SailboatToUmbrella,
    SailboatToBasketballHoop,
)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

matplotlib.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots()
fig.set_size_inches(18, 12)
ax.set_aspect(aspect='equal')

FONTSIZE=60
LANDMARK_ZOOM=60
LEGEND_IMAGE_STRETCH=(-17, 7.5)
LEGEND_IMAGE_OFFSET=(-8, 4)

draw_kwargs = {
    'depth_distance': 0.70 * FONTSIZE,
    'depth_fontsize': 0.25 * FONTSIZE,
    'draw_tieoffs': False,
    'include_depth': True,
    'include_mooringblocks': False,
    'include_text': False,
    'landmark_markersize': 10,
    'landmark_zoom': LANDMARK_ZOOM,
    'linewidth': 1,
    'text_fontsize': 13,
    'tieoff_size': 4.5,
}

######
#
# Draw the recreational area, forcing both the right loop and the left loop to close up
#
#####

draw(ax, Landmark.BAR, BarToPlatform, **draw_kwargs)

draw_circuit(ax, Landmark.SKELETON, SkeletonToMooringBlock2ViaPokerRun, SkeletonToMooringBlock2ViaMooringBlocks, **draw_kwargs)

draw(ax, Landmark.ANCHOR, AnchorToSailboat, **draw_kwargs)

draw(ax, Landmark.MOORING_BLOCK_2, MooringBlock2ToMooringBlock1, **draw_kwargs)

draw_circuit(ax, Landmark.MOORING_BLOCK_1, MooringBlock1ToMooringBlock5ViaPokerRun, MooringBlock1ToMooringBlock5ViaMooringBlocks, **draw_kwargs)

draw(ax, Landmark.UMBRELLA, UmbrellaToOxygenTanks, **draw_kwargs)

draw_between_landmarks(ax, Landmark.SAILBOAT, Landmark.SAILBOATTOUMBRELLASTAKE, SailboatToUmbrella, **draw_kwargs)

draw_between_landmarks(ax, Landmark.SAILBOAT, Landmark.UMBRELLA, SailboatToBasketballHoop, **draw_kwargs)

draw_between_landmarks(ax, Landmark.CONROY, Landmark.OXYGEN_TANKS, ConroyToOxygenTanks, **draw_kwargs)

draw(ax, Landmark.CAR, CarToLisasGift, **draw_kwargs)

draw(ax, Landmark.LISAS_GIFT, LisasGiftToKibbetts, **draw_kwargs)

draw(ax, Landmark.ANGLE_IRON, AngleIronToMary, **draw_kwargs)

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
y_max = y_max + 150
y_min = y_min - 300
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

draw_platforms(fontsize=None)
draw_boat_ramp()
draw_scale(corner_coordinates=((x_min, y_min), (x_max, y_max)), fontsize=0.25 * FONTSIZE, feet=(0, 100, 200, 300, 400), meters=(0, 25, 50, 75, 100))
draw_compass_rose(ax, corner_coordinates=((x_min, y_min), (x_max, y_max)), zoom=0.1)

#####
#
# Create the legend
# TODO(stpyang): put this in a different file
#
#####

BASKETBALL = Line2D([0], [0], label='Basketball hoop')
GIFT = Line2D([0], [0], label='Lisa\'s Gift')
KIBBETTS = Line2D([0], [0], label='Kibbett\'s')
OXYGEN = Line2D([0], [0], label='Oxygen bottles')
MARY = Line2D([0], [0], label='Mary')
SAILBOAT = Line2D([0], [0], label='Sailboat')
WHEEL = Line2D([0], [0], label='Wagon wheels')

basketball_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-384-basketball@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
kibbetts_handler = ImageHandler(image_path='icons/shipwreck.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
mary_handler = ImageHandler(image_path='icons/mary.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
sailboat_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-408-sailboat@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png', image_stretch=LEGEND_IMAGE_STRETCH, image_offset=LEGEND_IMAGE_OFFSET)

ax.legend(
    framealpha=0.0,
    fontsize=0.30 * FONTSIZE,
    handles=[
        BASKETBALL,
        GIFT,
        KIBBETTS,
        OXYGEN,
        MARY,
        SAILBOAT,
        WHEEL,
    ],
    handler_map={
        GIFT: gift_handler,
        KIBBETTS: kibbetts_handler,
        OXYGEN: oxygen_handler,
        MARY: mary_handler,
        SAILBOAT: sailboat_handler,
        WHEEL: wheel_handler,
        },
    labelspacing=0.6,
    loc='lower right')

plt.savefig('maps/rec_survey_2.png', transparent=True)
