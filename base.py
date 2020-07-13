from math import cos, pi, sin

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.image import BboxImage
from matplotlib.legend_handler import HandlerBase
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.transforms import Bbox, TransformedBbox

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

def __radians(degrees):
    return pi / 2 - float(degrees) / 360 * 2 * pi

def draw(ax, draw_distance, input_total_surveyed, input_corner_coordinates, landmark_coordinates, input_landmark, input_data):
    ((x_min, y_min), (x_max, y_max)) = input_corner_coordinates
    curser = landmark_coordinates[input_landmark]
    total_surveyed = input_total_surveyed
    for data in input_data:
        clazz = type(data).__name__
        if clazz == 'SurveyedLine' or clazz == 'UnsurveyedLine' or clazz == 'RemovedLine':
            (x0, y0) = curser
            length = data.length_ft + data.length_in / 12
            (x1, y1) = (x0 + length * cos(__radians(data.angle)), y0 + length * sin(__radians(data.angle)))
            plt.plot([x0, x1], [y0, y1], color=data.color, linestyle=data.linestyle, linewidth=2)
            mid_x = (x0 + x1) / 2 + 8 * sin(__radians(data.angle))
            mid_y = (y0 + y1) / 2 - 8 * cos(__radians(data.angle))
            mid_x = (x0 + x1) / 2 + 8 * sin(__radians(data.angle))
            mid_y = (y0 + y1) / 2 - 8 * cos(__radians(data.angle))
            if (data.flip_text_side):
                mid_x = (x0 + x1) / 2 - 8 * sin(__radians(data.angle))
                mid_y = (y0 + y1) / 2 + 8 * cos(__radians(data.angle))                
            if data.alt_text is None and draw_distance:
                text = '{}\''.format(data.length_ft)
                if data.length_in:
                    text = '{} {}\"'.format(text, data.length_in)
                text_rotation = (45 - data.angle) % 90 - 45
                plt.text(s=text, x=mid_x, y=mid_y, ha='center', rotation=text_rotation, fontsize=9, va='center')
            else:
                text = data.alt_text
                text_rotation = data.text_rotation
                if text_rotation is None:
                   text_rotation = (180 - data.angle) % 180 - 90
                plt.text(s=text, x=mid_x, y=mid_y, ha='center', rotation=text_rotation, fontsize=9, va='center')
            if data.include_in_total_surveyed:
                total_surveyed += length
            curser=(x1, y1)
        elif clazz == 'Arrow':
            (x0, y0) = curser
            (x1, y1) = (x0 + data.distance * cos(__radians(data.angle)), y0 + data.distance * sin(__radians(data.angle)))
            plt.plot(x1, y1, color='black', marker=(3, 0, -data.angle), markerfacecolor=data.color, markersize=7, zorder=3)
        elif clazz == 'SaveLandmark':
            landmark_coordinates[data.landmark] = curser
            if data.icon_path:
                (x, y) = curser
                plt.plot(x, y, color='white', marker='o', markersize=16, zorder=3)
                im = OffsetImage(plt.imread(data.icon_path), zoom=data.zoom/ax.figure.dpi)
                im.image.axes = ax
                im_ab = AnnotationBbox(im, landmark_coordinates[data.landmark], frameon=False)
                ax.add_artist(im_ab)
        elif clazz == 'Jump':
            (x0, y0) = curser
            length = data.length_ft + data.length_in / 12
            (x1, y1) = (x0 + length * cos(__radians(data.angle)), y0 + length * sin(__radians(data.angle)))
            curser = (x1, y1)
        elif clazz == 'Stake':
            (x, y) = curser
            plt.plot(x, y, color=data.color, marker=data.marker, markersize=5, zorder=data.zorder)
            if data.text is not None:
                plt.text(s=data.text, x=x, y=y, ha='center', va='center', rotation=data.text_rotation)
        elif clazz == 'TieOff':
            (x, y) = curser
            plt.plot(x, y, color=data.color, marker=data.marker, markersize=6, zorder=data.zorder)
        else:
            raise Exception('{} is not a recognized data class'.format('clazz'))
        (x, y) = curser
        x_min = min(x, x_min)
        x_max = max(x, x_max)
        y_min = min(y, y_min)
        y_max = max(y, y_max)
    return (total_surveyed, ((x_min, y_min), (x_max, y_max)), landmark_coordinates)
