def Qc_fit(x, a, b, c, d, e, f, g, h, i, k):
    """
    Fourth-order polynomial fit for slope and y-intercept of linear Qc/dT relationship
    :param x: (2, M) shaped array of independent variables I and dT. x[0, :] = I; x[1, :] = dT
    :param a-k: fitting coefficients
    :return: Qc(I, dT)
    """
    x1 = x[0] # I
    x2 = x[1] # dT
    m = (i * x1 ** 4 + a * x1 ** 3 + b * x1 ** 2 + c * x1 + d)
    b = (k * x1 ** 4 + e * x1 ** 3 + f * x1 ** 2 + g * x1 + h)
    return m * x2 + b

def Qc(I, dT, a, b, c, d, e, f, g, h, i, k):
    """
    Same as above, but with I and dT broken out of the first argument, x. More convenient to use this one.
    :param I: single value or ndarray shape (M, )
    :param dT: single value or ndarray shape (M, )
    """
    x1 = I # I
    x2 = dT # dT
    m = (i * x1 ** 4 + a * x1 ** 3 + b * x1 ** 2 + c * x1 + d)
    b = (k * x1 ** 4 + e * x1 ** 3 + f * x1 ** 2 + g * x1 + h)
    return m * x2 + b

def V_fit(x, a, b, c, d, e, f):
    """
    Second-order polynomial fit for slope and y-intercept of linear Qc/dT relationship
    :param x: (2, M) shaped array of independent variables I and dT. x[0, :] = I; x[1, :] = dT
    :param a-f: fitting coefficients
    :return: V(I, dT)
    """
    x1 = x[0] # I
    x2 = x[1] # dT
    m = (a * x1 ** 2 + b * x1 + c)
    b = (d * x1 ** 2 + e * x1 + f)
    return m * x2 + b

def V(I, dT, a, b, c, d, e, f):
    """
    Same as above, but with I and dT broken out of the first argument, x. More convenient to use this one.
    :param I: single value or ndarray shape (M, )
    :param dT: single value or ndarray shape (M, )
    """
    x1 = I # I
    x2 = dT # dT
    m = (a * x1 ** 2 + b * x1 + c)
    b = (d * x1 ** 2 + e * x1 + f)
    return m * x2 + b