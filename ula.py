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


def convert_output(intval):
    positivebin = '{0:b}'.format(abs(intval)).zfill(16)
    outputbin = ''

    if intval < 0:
        for c in positivebin:
            if c == '1':
                outputbin += '0'
            else:
                outputbin += '1'
        outputbin = '{0:b}'.format(int(outputbin, 2) + 1).zfill(16)
    else:
        outputbin = positivebin

    return outputbin