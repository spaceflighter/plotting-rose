from bokeh.plotting import figure, show
import math
import numpy as np
import random

def get_circle_coords(r, max_deg, sep):
    xs = []
    ys = []
    for deg in np.arange(0.0, max_deg, sep):
        rad = math.radians(deg)
        x = r * math.cos(rad)
        y = r * math.sin(rad)
        xs.append(x)
        ys.append(y)

    return (xs, ys)

def draw(ratios, radiuses, tick):
    ratio_coords = []
    for i in range(0, len(ratios)):
        ratio = ratios[i]
        max_deg = ratio * 360
        sep = max_deg / tick
        ratio_coord = get_circle_coords(radiuses[i], max_deg, sep)
        ratio_coords.append(ratio_coord)

    lengths = []
    for ratio_coord in ratio_coords:
        lengths.append(len(ratio_coord[0]))
    iter = min(lengths)
    p = figure(title = "Rose of Venus", x_axis_label = "x", y_axis_label = "y")
    for i in range(0, iter):
        xs = []
        ys = []
        for ratio_coord in ratio_coords:
            xs.append(ratio_coord[0][i])
            ys.append(ratio_coord[1][i])

        r = 237
        g = 149
        b = 147

        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)

        p.line(xs, ys, line_width = 0.5, color = (r, g, b))
    show(p)

def main():
    ratio = [8, 13]
    radius = [100, 70]
    num_lines = 2000
    draw(ratio, radius, num_lines)
    # draw([8, 13, 21], [100, 30, 10], 1000)

if __name__ == '__main__':
    main()