# calc_sqr_rt is to give the square root of a input if it is a number
def calc_sqr_rt(value):
    try:
        num = float(value)
        if num < 0:
            raise ValueError("Input must be a non-negative number.")
        return num ** 0.5
    except (ValueError, TypeError):
        return "Input must be a number."