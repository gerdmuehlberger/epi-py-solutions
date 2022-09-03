import collections
Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    if (r1.x <= r2.x + r2.width and 
    r1.x + r1.width >= r2.x and 
    r1.y + r1.height >= r2.y and 
    r1.y <= r2.y + r2.height):
        print("intersect")
        max_x = max(r1.x, r2.x)
        max_y = max(r1.y, r2.y)
        intersect_width = min(r1.x+r1.width, r2.x+r2.width) - max(r1.x, r2.x)
        intersect_height = min(r1.y+r1.height, r2.y+r2.height) - max(r1.y, r2.y)

        return Rect(max_x, max_y, intersect_width, intersect_height)
    else:
        print("no intersect")
        return Rect(0, 0, -1, -1)