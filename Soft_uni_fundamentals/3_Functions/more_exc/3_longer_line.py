from math import floor, sqrt


def calc_line_length(x1, y1, x2, y2):
    length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return length


def calc_point_distance(x, y):
    distance = sqrt(x ** 2 + y ** 2)
    return distance


def first_is_closer_point(x1, y1, x2, y2):
    dis1 = calc_point_distance(x1, y1)
    dis2 = calc_point_distance(x2, y2)
    if dis2 < dis1:
        return False
    else:
        return True


def center_points_line():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    a2 = float(input())
    b2 = float(input())
    c2 = float(input())
    d2 = float(input())
    total1 = calc_line_length(a, b, c, d)
    total2 = calc_line_length(a2, b2, c2, d2)
    # if total1 < total2:
    #     return f"({floor(a2)}, {floor(b2)})({floor(c2)}, {floor(d2)})"
    # else:
    #     return f"({floor(a)}, {floor(b)})({floor(c)}, {floor(d)})"
    if total2 > total1:
        if first_is_closer_point(a2, b2, c2, d2):
            return f"({floor(a2)}, {floor(b2)})({floor(c2)}, {floor(d2)})"
        else:
            return f"({floor(c2)}, {floor(d2)})({floor(a2)}, {floor(b2)})"
    else:
        if first_is_closer_point(a, b, c, d):
            return f"({floor(a)}, {floor(b)})({floor(c)}, {floor(d)})"
        else:
            return f"({floor(c)}, {floor(d)})({floor(a)}, {floor(b)})"


print(center_points_line())
