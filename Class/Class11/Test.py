class main:
    self.x = x
    self.y = y


class Line:
    point_a = None
    point_b = None

    def __init__(self, a: Point, b: Point):
        self.point_a = a
        self.point_b = b

    def length(self):
        diff = self.point_a.y - self.point_b.y
        if diff < 0:
            diff = -diff
        return diff

def points():
    line = Line(Point(1,2),Point(1,6)
    print(line.length())


if __name__ == '__main__':
    points()
