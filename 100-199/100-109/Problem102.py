from time import clock


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds" % (clock() - start))

    return wrapper


@timer
def find_answer():
    total = 0
    with open("triangles.txt") as f:
        for line in f:
            current = [float(x) for x in line.rstrip().split(",")]
            if barycentric(current):
                total += 1
    return total


def barycentric(points):
    px, py = 0.0, 0.0
    p1x, p1y = points[0], points[1]
    p2x, p2y = points[2], points[3]
    p3x, p3y = points[4], points[5]

    alpha = ((p2y - p3y) * (px - p3x) + (p3x - p2x) * (py - p3y)) / (
    (p2y - p3y) * (p1x - p3x) + (p3x - p2x) * (p1y - p3y))
    beta = ((p3y - p1y) * (px - p3x) + (p1x - p3x) * (py - p3y)) / (
    (p2y - p3y) * (p1x - p3x) + (p3x - p2x) * (p1y - p3y))
    gamma = 1.0 - alpha - beta

    if alpha > 0 and beta > 0 and gamma > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    find_answer()

