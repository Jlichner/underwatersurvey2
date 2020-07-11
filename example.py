from base import draw
from data import ExampleData, Landmark

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
ax.set_aspect(aspect='equal')

total_surveyed = 0
corner_coordinates = ((0, 0), (0, 0))
landmark_coordinates = dict()
landmark_coordinates[Landmark.MOORING_BLOCK] = (0, 0)

(total_surveyed, corner_coordinates, landmark_coordinates) = draw(ax, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.MOORING_BLOCK, ExampleData)

((x_min, y_min), (x_max, y_max)) = corner_coordinates
plt.axis('off')
plt.title('A fictional survey using example data')
plt.xlim(x_min - 10, x_max + 10)
plt.ylim(y_min - 10, y_max + 10)

plt.savefig('example.png')
