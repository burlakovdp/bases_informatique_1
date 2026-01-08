def cord_transformer(x0, y0):
    if x0 > 19 or x0 < 1:
        return -1
    if y0 > 19 or y0 < 1:
        return -1
    res_x = 70 + (x0-1)*35
    res_y = 630 - (y0-1)*35 
    return (res_x, res_y)