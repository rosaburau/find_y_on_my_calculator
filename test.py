import math

inp1 = input("coordinates pls: ").split()
floats = [float(x) for x in inp1]

x11 = floats[0]
y11 = floats[1]
x22 = floats[2]
y22 = floats[3]


def find_mx(x1, y1, x2, y2):
    mid_x = (x2 + x1) / 2
    mid_y = (y2 + y1) / 2

    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1

    perp_m = (-1)/m
    cc = mid_y - perp_m*mid_x

    d = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    distance = math.sqrt(d)

    def final_c():
        if c > 0:
            return " + " + str(c)
        elif c < 0:
            return " " + str(c)
        elif c == 0:
            return " "

    def final_cc():
        if cc > 0:
            return " + " + str(cc)
        elif cc < 0:
            return " " + str(cc)
        elif cc == 0:
            return " "

    return "f(x)= " + str(m) + "x" + str(final_c()) + "\n" + "perpendicular f(x)= " + str(perp_m) + str(final_cc()) + "\n" + "midpoint= (" + str(mid_x) + ";" + str(mid_y) + ")" + "\n" + "distance= " + str(distance)


print(find_mx(x11, y11, x22, y22))
