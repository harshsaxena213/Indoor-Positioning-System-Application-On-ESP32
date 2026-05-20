#d1 d2 and d3 are distances of anchors calculated after using kalman filter on raw rssi 
 

def trilateration(x1, y1, d1,
                  x2, y2, d2,
                  x3, y3, d3):

    #EQ1(After Subtracting Circle Eq)
    A = 2 * x2 - 2 * x1
    B = 2 * y2 - 2 * y1
    C = d1**2 - d2**2 - x1**2 + x2**2 - y1**2 + y2**2

    #EQ2(After Subtracting Circle Eq)
    D = 2 * x3 - 2 * x2
    E = 2 * y3 - 2 * y2
    F = d2**2 - d3**2 - x2**2 + x3**2 - y2**2 + y3**2

    dn = (A * E - B * D)

    #Zero Divsion Prevension
    if dn == 0:
        return None


    x = (C * E - F * B) / dn
    y = (A * F - D * C) / dn

    return (x, y)
