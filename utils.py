def lerp(a, b, t):
    return a + (b - a) * t

def get_intersection(p1, p2, p3, p4):
    den = (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0])
    if den == 0:
        return None

    t = ((p1[0] - p3[0]) * (p3[1] - p4[1]) - (p1[1] - p3[1]) * (p3[0] - p4[0])) / den
    u = -((p1[0] - p2[0]) * (p1[1] - p3[1]) - (p1[1] - p2[1]) * (p1[0] - p3[0])) / den

    if 0 <= t <= 1 and 0 <= u <= 1:
        intersection = (
            p1[0] + t * (p2[0] - p1[0]),
            p1[1] + t * (p2[1] - p1[1])
        )
        return {
            "x": intersection[0],
            "y": intersection[1],
            "offset": t
        }

    return None