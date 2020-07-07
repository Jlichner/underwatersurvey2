from base import draw
from data import Landmark, PokerRun, CarToKibbetts, UmbrellaToRockIsland, UmbrellaToOxygenTanks, RockIslandTNorthwest, RockIslandTSoutheast

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerBase
from matplotlib.image import BboxImage
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib._png import read_png

matplotlib.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots()
fig.set_size_inches(36, 24)
ax.set_aspect(aspect='equal')

total_surveyed = 0
corner_coordinates = ((0, 0), (0, 0))
landmark_coordinates = dict()
landmark_coordinates[Landmark.MOORING_BLOCK] = (0, 0)

(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.MOORING_BLOCK, PokerRun)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.CAR, CarToKibbetts)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.UMBRELLA, UmbrellaToOxygenTanks)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.UMBRELLA, UmbrellaToRockIsland)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.ROCK_ISLAND_T, RockIslandTNorthwest)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.ROCK_ISLAND_T, RockIslandTSoutheast)

((x_min, y_min), (x_max, y_max)) = corner_coordinates
plt.axis('off')
plt.title('Copyright 2020 NEUE. All Rights Reserved.', fontsize=24)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#####
#
# Create the legend
#
#####

HOME_ARROW = Line2D([0], [0], label='Home Arrow', color='black', linewidth=0, marker='^', markersize=7, markerfacecolor='white')
# PLATFORM = Patch(label='Platform', facecolor='darkgoldenrod')
TIE_OFF = Line2D([0], [0], label='Tie Off', color='blue', linewidth=0, marker='h', markersize=5)
STAKE = Line2D([0], [0], label='Stake', color='brown', linewidth=0, marker='s', markersize=5)
SURVEYED_LINE = Line2D([0], [0], label='Surveyed Line', color='black', linestyle='solid')
UNSURVEYED_LINE = Line2D([0], [0], label='Unsurveyed Line', color='black', linestyle='dotted')
REMOVED_LINE = Line2D([0], [0], label='Removed Line', color='lightgrey', linestyle='solid')

SKELETON = Line2D([0], [0], label='Skeleton')
CAR = Line2D([0], [0], label='Car')
UMBRELLA = Line2D([0], [0], label='Umbrella')
ANCHOR = Line2D([0], [0], label='Anchor')
WHEEL = Line2D([0], [0], label='Wagon wheels')
GIFT = Line2D([0], [0], label='Lisa\'s Gift')
ROWBOAT = Line2D([0], [0], label='Rowboat')
OXYGEN = Line2D([0], [0], label='Oxygen bottles')

class ImageHandler(HandlerBase):

    def __init__(self, xpad=0., ypad=0., update_func=None, image_path=None, image_stretch=(0, 0), image_offset=(0, 0)):
        super(ImageHandler, self).__init__(xpad, ypad, update_func)
        self.image_data = plt.imread(image_path)
        self.image_stretch = image_stretch
        self.image_offset = image_offset

    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize,
                       trans):

        # enlarge the image by these margins
        sx, sy = self.image_stretch
        ox, oy = self.image_offset

        # create a bounding box to house the image
        bb = Bbox.from_bounds(xdescent - sx + ox,
                              ydescent - sy + oy,
                              width + sx,
                              height + sy)

        tbb = TransformedBbox(bb, trans)
        image = BboxImage(tbb)
        image.set_data(self.image_data)

        self.update_prop(image, orig_handle, legend)

        return [image]

skeleton_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
car_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
umbrella_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
anchor_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
wheel_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
gift_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))
rowboat_handler = ImageHandler(image_path='icons/rowboat.png', image_stretch=(11, 26), image_offset=(6, 12))
oxygen_handler = ImageHandler(image_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png', image_stretch=(-2, 10), image_offset=(0, 5))

ax.legend(
    handles=[STAKE, TIE_OFF, HOME_ARROW, SURVEYED_LINE, UNSURVEYED_LINE, REMOVED_LINE, SKELETON, CAR, UMBRELLA, ANCHOR, WHEEL, GIFT, ROWBOAT, OXYGEN],
    handler_map={
        SKELETON: skeleton_handler,
        CAR: car_handler,
        UMBRELLA: umbrella_handler,
        ANCHOR: anchor_handler,
        WHEEL: wheel_handler,
        GIFT: gift_handler,
        ROWBOAT: rowboat_handler,
        OXYGEN: oxygen_handler,},
    fontsize=10,
    labelspacing=1.2,
    loc='lower right')

print('{} total line surveyed'.format(total_surveyed))

plt.savefig('survey.pdf')
