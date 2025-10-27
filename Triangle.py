# -*- coding: utf-8 -*-
"""
Fixed implementation of classifyTriangle(a, b, c)
Return values (must match legacy tests exactly):
  - 'Equilateral', 'Isoceles', 'Scalene', 'NotATriangle', 'Right', 'InvalidInput'
"""

def classifyTriangle(a, b, c):
    # ---- Input validation ----
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # ---- Triangle inequality ----
    if not (a + b > c and a + c > b and b + c > a):
        return 'NotATriangle'

    # ---- Classification ----
    if a == b == c:
        return 'Equilateral'

    sides = sorted([a, b, c])
    if sides[0]*sides[0] + sides[1]*sides[1] == sides[2]*sides[2]:
        return 'Right'

    if a == b or b == c or a == c:
        return 'Isoceles'

    return 'Scalene'
