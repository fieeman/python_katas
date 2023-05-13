'''
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with "*" character.
'''

def tower_builder(n_floors):
    # build here
    tower = []
    for i in range(n_floors):
        base = 2 * n_floors - 1
        m_factor = (2 * i + 1)
        tower.append(f"{'*' * m_factor:^{base}}")
    return tower