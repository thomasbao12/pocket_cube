from sympy.combinatorics import Permutation

'''
F = Permutation(2, 19, 21, 8)(3, 17, 20, 10)(4, 6, 7, 5)
R = Permutation(1, 5, 21, 14)(3, 7, 23, 12)(8, 10, 11, 9)
D = Permutation(6, 18, 14, 10)(7, 19, 15, 11)(20, 22, 23, 21)
'''
#https://www.sfu.ca/~jtmulhol/math302/puzzles-pc.html
R = Permutation(13,14,16,15)(10,2,19,22)(12,4,17,24)
U = Permutation(1,2,4,3)(9,5,17,13)(10,6,18,14)
F = Permutation(9,10,12,11)(3,13,22,8)(4,15,21,6)
D = Permutation(21,22,24,23)(11,15,19,7)(12,16,20,8)

def commutator(x, y):
    return x * y * ~x * ~y

def support(x, y):
    return set(x.support()).intersection(y.support())

def cycle_structure_size(x):
    return sum([
        k * v
        for k, v in x.cycle_structure.items()
        if k > 1
    ])


def visit(n):
    cool_moves = list()
    visited = set()
    unvisited = [('F', F), ('R', R), ('D', D)]
    while(unvisited and len(visited) < n):
        rep, perm = unvisited.pop(0)
        if perm in visited:
            continue
        # find interesting perms
        size = cycle_structure_size(perm)
        if size > 0 and size < 12:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print( "{}: {}".format(rep, size) )
            cool_moves.append(rep)
        for r, p in [('F', F), ('R', R), ('D', D)]:
            unvisited.append((rep + r, perm * p))
        visited.add(perm)

        if len(visited) % 1000 == 0:
            print(len(visited))
    return cool_moves
