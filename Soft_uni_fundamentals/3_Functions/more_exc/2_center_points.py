from math import floor
def center_points():
    point_x1 = float(input())
    point_y1 = float(input())
    point_x2 = float(input())
    point_y2 = float(input())
    total1 = abs(point_y1) + abs(point_x1)
    total2 = abs(point_y2) + abs(point_x2)
    if total2 < total1:
        print(f"({floor(point_x2)}, {floor(point_y2)})")
    elif total2 > total1 or total2 == total1:
        print(f"({floor(point_x1)}, {floor(point_y1)})")
center_points()
