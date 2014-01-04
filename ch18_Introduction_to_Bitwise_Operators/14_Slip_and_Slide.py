def flip_bit(number, n):
    return bin(number ^ (0b1 << (n-1)))