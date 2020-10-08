'''
Features of a Discrete Random Variable
- countable
- values are "discretized":
    - nothing in between the "discrete" values
    - 0.1, 0.2, 0.3 ... 10.0

Features of a Continuous Random Variable
- measurement problems
    - height of trees, building, etc
    - volume, mass, etc
- potential for infinite precision
    - if we have an infitinely precise instrument, we have "true continuity", an infinite of measurements between any two measurements.

Y_1 is a specific infinitely precise outcome from a continuous distribution with random variable Y. What is the probability of Y_1:  P(Y_1) = ?
0 because an infinitely precise value divided by an infinite number of outcomes is about as close to zero as you can get


in order to get a "specific" probability of a value from a continuous distribution, we in fact define a range.

CDF
to get the Proba of getting less than a given value
can also subtract two cdfs to get the probability of a range of values, thus discretizing our continuous distribution
'''




from random import choice

def get_bit():
    return choice([0,1])

def get_binary(n=8):
    # return [get_bit for _ in range(n)]
    return_list = []

    for _ in range(n):
        return_list.append(get_bit())
    
    return return_list

# print(get_binary(32))

def get_float(n=8):
    bin_list = get_binary(n)

    float_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5**idx

    return float_accum

# print(get_float(32))

def get_range(n=8, num_samples=10000):
    high = get_float(n)
    low = get_float(n)

    for _ in range(num_samples):
        flt = get_float(n)
        if flt > high:
            high = flt
        if flt < low:
            low = flt
    return low, high

print(get_range(n=8, num_samples=10000))