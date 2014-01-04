def distance_from_zero(para):
    tp = type(para);
    if tp == int or tp == float:
        return abs(para)
    else:
        return "Not an integer or float!"