from main import equalisation

test = [(1, 1, 1, 1, 1), (0.1, 2, 12, '1', 0.1),(-1, -1, 'hbreghbghe', -1, 2),(-1, -1, 1, -1, -2), (-1, -1, -1, 1, 2), (1, 1, 0, 0, 1)]
def tests(tes):
    for i in tes:
        equalisation(*i)


if __name__ == '__main__':
    tests(test)
