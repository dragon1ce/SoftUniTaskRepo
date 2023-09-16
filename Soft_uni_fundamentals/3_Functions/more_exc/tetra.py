import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def find_longer_line():
    # Get user input for the coordinates of the four points
    x1 = float(input("Enter the x-coordinate of point 1: "))
    y1 = float(input("Enter the y-coordinate of point 1: "))
    x2 = float(input("Enter the x-coordinate of point 2: "))
    y2 = float(input("Enter the y-coordinate of point 2: "))
    x3 = float(input("Enter the x-coordinate of point 3: "))
    y3 = float(input("Enter the y-coordinate of point 3: "))
    x4 = float(input("Enter the x-coordinate of point 4: "))
    y4 = float(input("Enter the y-coordinate of point 4: "))

    # Calculate the lengths of both lines
    line1_length = calculate_distance(x1, y1, x2, y2)
    line2_length = calculate_distance(x3, y3, x4, y4)

    # Calculate the distances of the midpoints to the origin
    line1_midpoint_distance = calculate_distance((x1 + x2) / 2, (y1 + y2) / 2, 0, 0)
    line2_midpoint_distance = calculate_distance((x3 + x4) / 2, (y3 + y4) / 2, 0, 0)

    # Compare the distances to the origin and determine the longer line
    if line1_length >= line2_length and line1_midpoint_distance <= line2_midpoint_distance:
        return f"({x1}, {y1})({x2}, {y2})"
    elif line2_length > line1_length and line2_midpoint_distance < line1_midpoint_distance:
        return f"({x3}, {y3})({x4}, {y4})"
    else:
        return f"({x1}, {y1})({x2}, {y2})"

# Call the function to find the longer line based on user input
longer_line = find_longer_line()
print("The longer line is:", longer_line)
