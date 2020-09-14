def compute_ula(x, y, zx, zy, nx, ny, f, no):
    tx = x * (not zx)
    ty = y * (not zy)
    if nx:
        tx = -tx
    if ny:
        ty = -ty

    if f:
        to = tx + ty
    else:
        to = tx & ty

    if no:
        to = -to

    zr = int(to == 0)
    ng = int(to < 0)
    out = to
    return zr, ng, out