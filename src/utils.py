from PIL import Image, ImageTk
from pathlib import Path

def rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    # List of points for the rounding
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    # Return the created polygon by it's id
    return canvas.create_polygon(points, **kwargs, smooth=True)

def load_asset(path, resize=None):
    # Construct an independent path
    absolute = Path(__file__).parent / ("../assets/" + path)

    if resize == None:
        return ImageTk.PhotoImage(Image.open(absolute))
    else:
        return ImageTk.PhotoImage(Image.open(absolute).resize(resize))
