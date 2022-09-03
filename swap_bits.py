def swap_bits(x, i, j):
    n=0

    bit_i = (x >> i) & 1
    bit_j = (x >> j) & 1

    if bit_i is bit_j:
        n=x
    elif bit_i == 1 and bit_j == 0:
        n = x | (1 << j) 
        n = n & ~(1 << i)
    elif bit_i == 0 and bit_j == 1:
        n = x | (1 << i) 
        n = n & ~(1 << j)

    return n