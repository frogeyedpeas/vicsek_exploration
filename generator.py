import copy
def combine(matrix): #accepts a matrix of matrices and fuses them
    aggregate = []
    for row in matrix:
        for j in range(0, len(matrix[0][0])):
            agg_row = []
            for block in row:
                agg_row += block[j]
            aggregate.append(agg_row)
    return aggregate
def descend(seed, zero, source, bound): #general fractal constructor
    for i in range(0, bound):
        for q in range(0, len(source)):
            for r in range(0, len(source[q])):
                if source[q][r] == 1:
                    source[q][r] = copy.deepcopy(seed)
                if source[q][r] == 0:
                    source[q][r] = copy.deepcopy(zero)
        source = combine(source) #fuse it up
    return source
def count(matrix, bound):
    counter = 0
    center_x, center_y = len(matrix)//2, len(matrix)//2
    shift_limit = bound//2
    if len(matrix)%2 == 1 and bound % 2 == 1:
        for i in range(-shift_limit, shift_limit+1):
            for j in range(-shift_limit, shift_limit+1):
                if matrix[center_x+i][center_y+j] == 1:
                    counter += 1
    if len(matrix)%2 == 1 and bound % 2 == 0:
        for i in range(-shift_limit, shift_limit):
            for j in range(-shift_limit, shift_limit):
                if matrix[center_x+i][center_y+j] == 1:
                    counter += 1
    return counter
seed = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
source = [[1]]
zero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#example with n=5
n=5
#print(count(descend(seed, zero, source, 2), 5)) #this constructs a 3^2 X 3^2 matrix and counts the center 5 X 5 matrix

structure = descend(seed, zero, source, 6)

sol = []
for i in range(0, 3**6+1):
    sol.append(count(structure, i))

print(sol)


