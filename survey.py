from base import draw
from data import Landmark, PokerRun, CarToKibbetts, UmbrellaToRockIsland, UmbrellaToOxygenTanks, RockIslandTNorthwest, RockIslandTSoutheast

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

fig, ax = plt.subplots()
fig.set_size_inches(36, 24)
ax.set_aspect(aspect='equal')

total_surveyed = 0
corner_coordinates = ((0, 0), (0, 0))
landmark_coordinates = dict()
landmark_coordinates[Landmark.MOORING_BLOCK] = (0, 0)

(total_surveyed, corner_coordinates, landmark_coordinates) = draw(plt, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.MOORING_BLOCK, PokerRun)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(plt, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.CAR, CarToKibbetts)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(plt, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.UMBRELLA, UmbrellaToOxygenTanks)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(plt, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.UMBRELLA, UmbrellaToRockIsland)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(plt, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.ROCK_ISLAND_T, RockIslandTNorthwest)
(total_surveyed, corner_coordinates, landmark_coordinates) = draw(plt, total_surveyed, corner_coordinates, landmark_coordinates, Landmark.ROCK_ISLAND_T, RockIslandTSoutheast)

###
# Create the legend
###
HOME_ARROW = Line2D([0], [0], label='Home Arrow', color='black', linewidth=0, marker='^', markersize=6, markerfacecolor='white')
# PLATFORM = Patch(label='Platform', facecolor='darkgoldenrod')
TIE_OFF = Line2D([0], [0], label='Tie Off', color='blue', linewidth=0, marker='h', markersize=4)
STAKE = Line2D([0], [0], label='Stake', color='brown', linewidth=0, marker='s', markersize=4)
SURVEYED_LINE = Line2D([0], [0], label='Surveyed Line', color='black', linestyle='solid')
UNSURVEYED_LINE = Line2D([0], [0], label='Unsurveyed Line', color='black', linestyle='dotted')
REMOVED_LINE = Line2D([0], [0], label='Removed Line', color='lightgrey', linestyle='solid')

((x_min, y_min), (x_max, y_max)) = corner_coordinates
# plt.axis('off')
plt.xlim(x_min - 50, x_max + 50)
plt.ylim(y_min - 50, y_max + 50)
ax.legend(handles=[STAKE, TIE_OFF, HOME_ARROW, SURVEYED_LINE, UNSURVEYED_LINE, REMOVED_LINE], fontsize=9, loc='lower right')

trans_x, trans_y = ax.transData.transform(landmark_coordinates[Landmark.SKELETON])
plt.figimage(X=plt.imread('glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull.png'), xo=trans_x, yo=trans_y)

print('{} total line surveyed'.format(total_surveyed))

plt.savefig('survey.pdf')
