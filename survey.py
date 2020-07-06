from base import draw
from data import Landmark, PokerRun, CarToKibbetts, UmbrellaToRockIsland, UmbrellaToOxygenTanks, RockIslandTNorthwest, RockIslandTSoutheast

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

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
plt.title('Copyright 2020 NEUE. All Rights Reserved.')
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

ax.legend(
	handles=[STAKE, TIE_OFF, HOME_ARROW, SURVEYED_LINE, UNSURVEYED_LINE, REMOVED_LINE],
	fontsize=9,
	loc='lower right')

print('{} total line surveyed'.format(total_surveyed))

plt.savefig('survey.pdf')
