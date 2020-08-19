from data import Landmark, SurveyedLine, UnsurveyedLine, Arrow, Jump, RemovedLine, RemovedStake, SaveLandmark

from math import atan, cos, pi, sin, sqrt

import matplotlib.pyplot as plt

from matplotlib.patches import Polygon
from matplotlib.collections import LineCollection
from matplotlib.image import BboxImage
from matplotlib.legend_handler import HandlerBase
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.transforms import Bbox, TransformedBbox

#####
#
# GLOBAL VARIABLES
#
#####

DRAW_DISTANCE = False
__LANDMARK_COORDINATES = dict()
__LANDMARK_COORDINATES[Landmark.BAR] = (0, 0)
__CORNER_COORDINATES = ((0, 0), (0, 0))
__TOTAL_SURVEYED = 0
# __MAGNETIC_DECLINATION = 12.58
__MAGNETIC_DECLINATION = 0


#####
#
# HELPER CLASS FOR THE LEGEND
#
#####

class ImageHandler(HandlerBase):

    def __init__(self, xpad=0., ypad=0., update_func=None, image_path=None, image_stretch=(-2, 10), image_offset=(0, 5)):
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

def __radians(degrees):
    return pi / 2 - float(degrees) / 360 * 2 * pi

def __degrees(radians):
    return (radians + pi / 2) / 2 / pi * 360

def __meters(meters):
    return meters * 3.28084

def draw_compass_rose():
    ((x_min, y_min), (x_max, y_max)) = __CORNER_COORDINATES
    (center_x, center_y) = ((0.9 * x_min + 0.1 * x_max), (0.1 * y_min + 0.9 * y_max))
    length = 100
    # magnetic_north_x = center_x + length * cos(__radians(-__MAGNETIC_DECLINATION))
    # magnetic_north_y = center_y + length * sin(__radians(-__MAGNETIC_DECLINATION))
    (north_x, north_y) = (center_x, center_y + length)
    (east_x, east_y) = (center_x + length, center_y)
    (south_x, south_y) = (center_x, center_y - length)
    (west_x, west_y) = (center_x - length, center_y)
    plt.plot([south_x, north_x], [south_y, north_y], color='black', linewidth='3', marker='^', markersize=10)
    plt.plot([west_x, east_x], [west_y, east_y], color='black', linewidth='2', marker=None)
    # plt.plot([center_x, magnetic_north_x], [center_y, magnetic_north_y], color='black', linewidth=3, marker = '^')
    plt.text(x=center_x + length / 16, y=center_y + length / 2, s='N', ha='left', va='center', fontsize='20')

def draw_scale():
    ((x_min, y_min), (x_max, y_max)) = __CORNER_COORDINATES
    (x, y) = ((0.9 * x_min + 0.1 * x_max) - __meters(100) / 2, (0.2 * y_min + 0.8 * y_max))

    # feet
    plt.text(s='0', x=x, y=y + 10, ha='center', fontsize=9, va='bottom')
    plt.plot([x, x + 50], [y, y], color='black', linewidth=2, marker=2)
    plt.text(s='50', x=(x + 50), y=y + 10, ha='center', fontsize=9, va='bottom')
    plt.plot([x + 50, x + 100], [y, y], color='black', linewidth=2, marker=2)
    plt.text(s='100', x=(x + 100), y=y + 10, ha='center', fontsize=9, va='bottom')
    plt.plot([x + 100, x + 200], [y, y], color='black', linewidth=2, marker=2)
    plt.text(s='200', x=(x + 200), y=y + 10, ha='center', fontsize=9, va='bottom')
    plt.plot([x + 200, x + 300], [y, y], color='black', linewidth=2, marker=2)
    plt.text(s='300', x=(x + 300), y=y + 10, ha='center', fontsize=9, va='bottom')
    plt.text(s='feet', x=(x + 250), y=y + 10, ha='center', fontsize=9, va='bottom')

    # meters
    plt.text(s='0', x=x, y=y - 10, ha='center', fontsize=9, va='top')
    plt.plot([x, x + __meters(10)], [y, y], color='black', linewidth=2, marker=3)
    plt.text(s='10', x=(x + __meters(10)), y=y - 10, ha='center', fontsize=9, va='top')
    plt.plot([x + __meters(10), x + __meters(20)], [y, y], color='black', linewidth=2, marker=3)
    plt.text(s='20', x=(x + __meters(20)), y=y - 10, ha='center', fontsize=9, va='top')
    plt.plot([x + __meters(20), x + __meters(30)], [y, y], color='black', linewidth=2, marker=3)
    plt.text(s='30', x=(x + __meters(30)), y=y - 10, ha='center', fontsize=9, va='top')
    plt.plot([x + __meters(30), x + __meters(50)], [y, y], color='black', linewidth=2, marker=3)
    plt.text(s='50', x=(x + __meters(50)), y=y - 10, ha='center', fontsize=9, va='top')
    plt.plot([x + __meters(50), x + __meters(100)], [y, y], color='black', linewidth=2, marker=3)
    plt.text(s='100', x=(x + __meters(100)), y=y - 10, ha='center', fontsize=9, va='top')
    plt.text(s='meters', x=(x + 250), y=y - 10, ha='center', fontsize=9, va='top')

def add_copyright():
    ((x_min, y_min), (x_max, y_max)) = __CORNER_COORDINATES
    plt.text(x_max, y_min - 100, 'Copyright 2020 NEUE.  All Rights Reserved.', fontsize=24, horizontalalignment='right')

def draw(ax, input_landmark, input_data, stretch = 1.0, rotation = 0.0):
    global __CORNER_COORDINATES, __LANDMARK_COORDINATES, __TOTAL_SURVEYED
    ((x_min, y_min), (x_max, y_max)) = __CORNER_COORDINATES
    curser = __LANDMARK_COORDINATES[input_landmark]
    for data in input_data:
        clazz = type(data).__name__
        if clazz == 'SurveyedLine' or clazz == 'UnsurveyedLine' or clazz == 'RemovedLine' or clazz == 'RemovedUnsurveyedLine':
            (x0, y0) = curser
            length = (data.length_ft + data.length_in / 12) * stretch
            angle = data.angle + rotation - __MAGNETIC_DECLINATION
            (x1, y1) = (x0 + length * cos(__radians(angle)), y0 + length * sin(__radians(angle)))
            plt.plot([x0, x1], [y0, y1], color=data.color, linestyle=data.linestyle, linewidth=2, zorder=1)
            mid_x = (x0 + x1) / 2 + 8 * sin(__radians(angle))
            mid_y = (y0 + y1) / 2 - 8 * cos(__radians(angle))
            mid_x = (x0 + x1) / 2 + 8 * sin(__radians(angle))
            mid_y = (y0 + y1) / 2 - 8 * cos(__radians(angle))
            if (data.flip_text_side):
                mid_x = (x0 + x1) / 2 - 8 * sin(__radians(angle))
                mid_y = (y0 + y1) / 2 + 8 * cos(__radians(angle))                
            if data.alt_text is None and DRAW_DISTANCE:
                text = '{}\''.format(data.length_ft)
                if data.length_in:
                    text = '{} {}\"'.format(text, data.length_in)
                text_rotation = (45 - angle) % 90 - 45
                plt.text(s=text, x=mid_x, y=mid_y, ha='center', rotation=text_rotation, fontsize=9, va='center')
            else:
                text = data.alt_text
                text_rotation = data.text_rotation
                if text_rotation is None:
                   text_rotation = (180 - angle) % 180 - 90
                plt.text(s=text, x=mid_x, y=mid_y, ha='center', rotation=text_rotation, fontsize=9, va='center')
            if data.include_in_total_surveyed:
                __TOTAL_SURVEYED += length
            curser = (x1, y1)
        elif clazz == 'Arrow':
            (x0, y0) = curser
            angle = data.angle + rotation - __MAGNETIC_DECLINATION
            (x1, y1) = (x0 + data.distance * cos(__radians(angle)), y0 + data.distance * sin(__radians(angle)))
            plt.plot(x1, y1, color='black', marker=(3, 0, -angle), markerfacecolor=data.color, markersize=7, zorder=3)
        elif clazz == 'SaveLandmark':
            __LANDMARK_COORDINATES[data.landmark] = curser
            if data.icon_path:
                (x, y) = curser
                plt.plot(x, y, color='white', marker='s', markersize=data.markersize, zorder=data.zorder)
                im = OffsetImage(plt.imread(data.icon_path), zoom=data.zoom/ax.figure.dpi)
                im.image.axes = ax
                im_ab = AnnotationBbox(im, __LANDMARK_COORDINATES[data.landmark], frameon=False)
                ax.add_artist(im_ab)
        elif clazz == 'Jump':
            (x0, y0) = curser
            length = float(data.length_ft + data.length_in / 12) * stretch
            angle = data.angle + rotation - __MAGNETIC_DECLINATION
            (x1, y1) = (x0 + length * cos(__radians(angle)), y0 + length * sin(__radians(angle)))
            curser = (x1, y1)
        elif clazz == 'Stake' or clazz == 'RemovedStake':
            (x, y) = curser
            plt.plot(x, y, color=data.color, marker=data.marker, markersize=data.markersize, zorder=data.zorder)
            if data.text is not None:
                plt.text(s=data.text, x=x, y=y, ha='center', va='center', rotation=data.text_rotation)
        elif clazz == 'TieOff':
            (x, y) = curser
            plt.plot(x, y, color=data.color, marker=data.marker, markersize=6, zorder=data.zorder)
        else:
            raise Exception('{} is not a recognized data class'.format(clazz))
        (x, y) = curser
        x_min = min(x, x_min)
        x_max = max(x, x_max)
        y_min = min(y, y_min)
        y_max = max(y, y_max)
    __CORNER_COORDINATES = ((x_min, y_min), (x_max, y_max))


def draw_circuit(ax, input_landmark, input_data_1, input_data_2):
    (distance_1, angle_1) = __survey_distance_angle(input_data_1)
    (distance_2, angle_2) = __survey_distance_angle(input_data_2)
    stretch_1 = 2 * distance_2 / (distance_1 + distance_2)
    stretch_2 = 2 * distance_1 / (distance_1 + distance_2)
    rotation_1 = (angle_1 - angle_2) / 2
    rotation_2 = (angle_2 - angle_1) / 2
    draw(ax=ax, input_landmark=input_landmark, input_data=input_data_1, stretch=stretch_1, rotation=rotation_1)
    draw(ax=ax, input_landmark=input_landmark, input_data=input_data_2, stretch=stretch_2, rotation=rotation_2)

def draw_between_landmarks(ax, landmark_0, landmark_1, input_data):
    (distance_1, angle_1) = __landmark_distance_angle(landmark_0, landmark_1)
    (distance_2, angle_2) = __survey_distance_angle(input_data)
    stretch = distance_1 / distance_2
    rotation = angle_2 - angle_1
    draw(ax=ax, input_landmark=landmark_0, input_data=input_data, stretch=stretch, rotation=rotation)

def __survey_distance_angle(input_data):
    curser = (0, 0)
    for data in input_data:
        clazz = type(data).__name__
        if clazz in ('SurveyedLine', 'UnsurveyedLine', 'RemovedLine', 'Jump'):
            (x0, y0) = curser
            length = data.length_ft + data.length_in / 12
            (x1, y1) = (x0 + length * cos(__radians(data.angle)), y0 + length * sin(__radians(data.angle)))
            curser = (x1, y1)
    (x, y) = curser
    distance = sqrt(x * x + y * y)
    if (x >= 0):
        angle = atan(y / x)
    else:
        angle = atan(y / x) + pi
    return (distance, __degrees(angle))

def __landmark_distance_angle(landmark_0, landmark_1):
    (x0, y0) = __LANDMARK_COORDINATES[landmark_0]
    (x1, y1) = __LANDMARK_COORDINATES[landmark_1]
    x = (x1 - x0)
    y = (y1 - y0)
    distance = sqrt(x * x + y * y)
    if (x >= 0):
        angle = atan(y / x)
    else:
        angle = atan(y / x) + pi
    return (distance, __degrees(angle))

def corner_coordinates():
    return __CORNER_COORDINATES

def total_surveyed():
    return __TOTAL_SURVEYED

def get_landmark_coordinates():
    return __LANDMARK_COORDINATES

def draw_platforms():
    length1= 15 + 9 / 12
    width1 = 11 + 2 / 12
    distance = 8 + 4 / 12
    length2 = 11 + 3 / 12
    width2 = 15 + 11 / 12
    angle = 330


    (x, y) = __LANDMARK_COORDINATES[Landmark.SKELETON]
    x -= 5 # fudge
    y -= 4 # fudge
    corners1 = [(x, y)]
    (x, y) = (x + length1 * cos(__radians(angle)),  y + length1 * sin(__radians(angle)))
    corners1 += [(x, y)]
    (x, y) = (x + width1 * cos(__radians(angle - 90)),  y + width1 * sin(__radians(angle - 90)))
    corners1 += [(x, y)]
    (x, y) = (x + length1 * cos(__radians(angle - 180)),  y + length1 * sin(__radians(angle - 180)))
    corners1 += [(x, y)]
    platform1 = Polygon(xy=corners1, closed=True, color='black')

    (x, y) = __LANDMARK_COORDINATES[Landmark.SKELETON]
    (x, y) = (x + length1 * cos(__radians(angle)),  y + length1 * sin(__radians(angle)))
    (x, y) = (x + distance * cos(__radians(angle)),  y + distance * sin(__radians(angle)))
    x -= 4 # fudge
    y -= 4 # fudge

    corners2 = [(x, y)]
    (x, y) = (x + length2 * cos(__radians(angle)),  y + length2 * sin(__radians(angle)))
    corners2 += [(x, y)]
    (x, y) = (x + width2 * cos(__radians(angle - 90)),  y + width2 * sin(__radians(angle - 90)))
    corners2 += [(x, y)]
    (x, y) = (x + length2 * cos(__radians(angle - 180)),  y + length2 * sin(__radians(angle - 180)))
    corners2 += [(x, y)]
    platform2 = Polygon(xy=corners2, closed=True, color='black')

    plt.gca().add_line(platform1)
    plt.gca().add_line(platform2)

def draw_boat_ramp():
    length = 100
    width = 35 + 10 / 12
    angle = 325
    (x, y) = __LANDMARK_COORDINATES[Landmark.BOAT_RAMP_2]
    corners = [__LANDMARK_COORDINATES[Landmark.BOAT_RAMP_1], __LANDMARK_COORDINATES[Landmark.BOAT_RAMP_2]]
    (x, y) = (x + length * cos(__radians(angle - 180)),  y + length * sin(__radians(angle - 180)))
    corners += [(x, y)]
    (x, y) = (x + width * cos(__radians(angle - 90)),  y + width * sin(__radians(angle - 90)))
    corners += [(x, y)]
    boat_ramp = Polygon(xy=corners, closed=True, color='lightgray')

    plt.gca().add_line(boat_ramp)