from cs1graphics import *

_canvas = None
_current_color = "black"
_current_line_thickness = 1
_cue = None

def open_canvas(width, height):
    """Creates a window for painting of a given width and height."""
    global _canvas
    if _canvas != None:
        raise RuntimeError("Canvas is already open.")
    _canvas = Canvas(width, height)

def clear_canvas():
    """Clears the canvas of all shapes and text."""
    global _canvas
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        _canvas.clear()

def set_line_thickness(thickness):
    """Sets the canvas painting line width to the integer given."""
    global _current_line_thickness
    _current_line_thickness = thickness

def set_color(color):
    """Sets the current painting color."""
    global _current_color
    _current_color = color

def set_color_rgb(r, g, b):
    """Sets the current painting color."""
    global _current_color
    _current_color = (r, g, b)

def _set_filled(shape):
    global _current_color
    shape.setBorderWidth(0)
    shape.setFillColor(_current_color)

def _set_not_filled(shape):
    global _current_color
    global _current_line_thickness
    shape.setBorderWidth(_current_line_thickness)
    shape.setBorderColor(_current_color)

def draw_circle(centerx, centery, radius):
    """Draws a circle on the canvas."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        circle = Circle()
        circle.move(centerx, centery)
        circle.setRadius(radius)
        _set_not_filled(circle)
        _canvas.add(circle)

def draw_filled_circle(centerx, centery, radius):
    """Draws a filled circle on the canvas."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        circle = Circle()
        circle.move(centerx, centery)
        circle.setRadius(radius)
        _set_filled(circle)
        _canvas.add(circle)


def draw_oval(centerx, centery, radiusx, radiusy):
    """Draws an oval on the canvas."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        oval = Ellipse(radiusx * 2, radiusy * 2, Point(centerx, centery))
        _set_not_filled(oval)
        _canvas.add(oval)

def draw_filled_oval(centerx, centery, radiusx, radiusy):
    """Draws a filled oval on the canvas."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        oval = Ellipse(radiusx * 2, radiusy * 2, Point(centerx, centery))
        _set_filled(oval)
        _canvas.add(oval)


def draw_line(x1, y1, x2, y2):
    """Draws a line on the canvas from (x1, y1) to (x2, y2)."""
    #global _canvas
    #global _current_line_thickness
    #global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        path = Path(Point(x1, y1), Point(x2, y2))
        path.setBorderWidth(_current_line_thickness)
        path.setBorderColor(_current_color)
        _canvas.add(path)

        
def draw_rect(x, y, width, height):
    """Draws a rectangle on the canvas. Upper left corner at (x, y), width
    and height as given."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        rect = Rectangle(width, height, Point(x+width/2, y+height/2))
        _set_not_filled(rect)
        _canvas.add(rect)

def draw_filled_rect(x, y, width, height):
    """Draws a filled rectangle on the canvas. Upper left corner at (x, y), width
    and height as given."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        rect = Rectangle(width, height, Point(x+width/2, y+height/2))
        _set_filled(rect)
        _canvas.add(rect)

def draw_polygon(*points):
    """Draws a polygon on the canvas.  The points of the polygon are (x,y) pairs
    specified as one big list.  E.g.: draw_polygon(10, 10, 20, 20, 30, 40) draws a
    polygon bounded by (10, 10) to (20, 20) to (30, 40) to (10, 10)."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        newpoints = []
        for x in range(0, len(points), 2):
            pt = Point(points[x], points[x+1])
            newpoints += [ pt ]
        polygon = Polygon(*newpoints)
        _set_not_filled(polygon)
        _canvas.add(polygon)

def draw_filled_polygon(*points):
    """Draws a filled polygon on the canvas.  The points of the polygon are (x,y) pairs
    specified as one big list.  E.g.: draw_polygon(10, 10, 20, 20, 30, 40) draws a
    polygon bounded by (10, 10) to (20, 20) to (30, 40) to (10, 10)."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        newpoints = []
        for x in range(0, len(points), 2):
            pt = Point(points[x], points[x+1])
            newpoints += [ pt ]
        polygon = Polygon(*newpoints)
        _set_filled(polygon)
        _canvas.add(polygon)
             
def draw_polyline(*points):
    """Draws a polyline on the canvas.  The points of the polyline are (x,y) pairs
    specified as one big list.  E.g.: draw_polyline(10, 10, 20, 20, 30, 40) draws a
    line from (10, 10) to (20, 20) to (30, 40)."""
    global _canvas
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        #print(points)
        #print(len(points))
        newpoints = []
        for x in range(0, len(points), 2):
            #print(x)
            pt = Point(points[x], points[x+1])
            newpoints += [ pt ]
            #print(newpoints)
        path = Path(*newpoints)
        path.setBorderWidth(_current_line_thickness)
        path.setBorderColor(_current_color)
        _canvas.add(path)
             

def draw_string(message, x, y, textSize):
    """Draws the message at the given location [(x, y) will be where the
    midpoint of the string ends up] with the given font size in points."""
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        t = Text(message, textSize)
        t.move(x, y)
        t.setFontColor(_current_color)
        _canvas.add(t)
        
def draw_image(imageName, x, y):
    """Draws the image centered at the given location
    [(x, y) will be where the midpoint of the image ends up] """
    global _canvas
    global _current_color
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        i = Image(imageName)
        i.move(x, y)
        _canvas.add(i)

def close_canvas():
    """Closes the canvas window immediately."""
    global _canvas
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        _canvas.close()
        _canvas = None

def close_canvas_after_click():
    """Sets the canvas window to close after the next mouse click anywhere on it."""
    global _canvas
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        wait_for_click()
        _canvas.close()
        _canvas = None

def set_background_color(color):
    """Sets the background color of the canvas.  Can be called at any time and the color will
    instantly change."""
    global _canvas
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        _canvas.setBackgroundColor(color)

def set_background_color_rgb(r, g, b):
    """Sets the background color of the canvas.  Can be called at any time and the color will
    instantly change."""
    global _canvas
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        _canvas.setBackgroundColor((r, g, b))

def save_canvas_as_image(filename):
    """Saves the image to the supplied filename, which must end in .ps or .eps"""
    global _canvas
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        _canvas.saveToFile(filename)

def wait_for_click():
    """This function just waits until the canvas is clicked.  After a mouse click, the program
    resumes."""
    global _canvas
    global _cue
    if _canvas == None:
        raise RuntimeError("Canvas is not open yet.")
    else:
        while True:
            _cue = _canvas.wait()
            if _cue.getDescription() == 'mouse release': break

def get_last_click_x():
    """Returns the x coordinate of the last mouse click that was waited for."""
    return _cue.getMouseLocation().getX()

def get_last_click_y():
    """Returns the y coordinate of the last mouse click that was waited for."""
    return _cue.getMouseLocation().getY()
