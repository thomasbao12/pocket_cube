# pocket_cube
Script to find interesting moves for a 2x2

A short script based on https://www.sfu.ca/~jtmulhol/math302/puzzles-pc.html which uses the sympy permutation library.

## Overview
1. Label each cube's face from 1 to 24
2. Describe rotations of each face as permutations of the numbered faces, using disjoint cycles/orbits.  (R is rotating the right face clockwise.  F and D, are rotating the front and bottom face clockwise, respectively)
3. Do a breadth first search of moves.  
4. Look at the cycle structure.  Permutations which permute fewer than 9 elements are interesting!

### Example
~100k permutations in, you'll get the first interesting move, FFRFRRDRDDFD, which cycles cubes, FLU, FLB, FRB.

### Extensions
This script will enumerate all possible states of a rubik's cube, modulo rotating the entire rubik's cube.

### Observations
Finally got to use Group Theory (even if it's just the intro bits)!

Moves that move fewer than 4 cubes are pretty rare.  I didn't hit the first one until 100k permutations in! 

Moves that move 2 cubes are super rare!

Most of these moves aren't commutators.  Probably more useful for larger cubes.

### Other readings

http://people.math.harvard.edu/~jjchen/docs/rubik.pdf
https://web.mit.edu/sp.268/www/rubik.pdf
