# Practical 1 :

import math
import cmath

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Not a quadratic equation (a cannot be 0).")
else:
    d = b**2 - 4*a*c   # discriminant

    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("Roots are real and distinct.")
        print("Root 1 =", r1)
        print("Root 2 =", r2)

    elif d == 0:
        r = -b / (2*a)
        print("Roots are real and equal.")
        print("Root 1 = Root 2 =", r)

    else:
        r1 = (-b + cmath.sqrt(d)) / (2*a)
        r2 = (-b - cmath.sqrt(d)) / (2*a)
        print("Roots are complex.")
        print("Root 1 =", r1)
        print("Root 2 =", r2)