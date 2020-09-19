

'''
Random Experiment
'''

from random import choice

def coin_flip():
    flip = choice(['H', 'T'])
    return flip

# 20 flips
twenty_flips = []

for _ in range(20):
    twenty_flips.append(coin_flip())

print(twenty_flips.count('H'))
print(twenty_flips.count('T'))