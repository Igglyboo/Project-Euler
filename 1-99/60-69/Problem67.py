from time import clock

tri = []

with open("triangle.txt") as f:
    for line in f:
        row = []
        for item in line.rstrip().split(" "):
            row.append(int(item))
        tri.append(row)


def timer(function):
    def wrapper(*args, **kwargs):
        start = clock()
        print(function(*args, **kwargs))
        print("Solution took: %f seconds." % (clock() - start))

    return wrapper


@timer
def find_answer():
    for row in range(len(tri) - 2, -1, -1):
        for col in range(len(tri[row])):
            if tri[row + 1][col] > tri[row + 1][col + 1]:
                tri[row][col] = tri[row][col] + tri[row + 1][col]
            else:
                tri[row][col] = tri[row][col] + tri[row + 1][col + 1]

    return tri[0][0]


if __name__ == "__main__":
    find_answer()

