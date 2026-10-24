
import sympy as sp
import numpy as np

# ---------- Symbols ----------
x, y, z = sp.symbols('x y z')

# ---------- Gradient of a scalar field ----------
def gradient(f, variables):
    # grad f = (df/dx, df/dy, df/dz)
    return sp.Matrix([sp.diff(f, v) for v in variables])


# ---------- 1. Scalar field in 3 variables ----------
print("=== 1. Gradient of f(x, y, z) = x^2*y + y*z^2 + sin(x*z) ===")
f1 = x**2 * y + y * z**2 + sp.sin(x * z)
g1 = gradient(f1, (x, y, z))
print("f =", f1)
print("grad f =", g1.T)

# value of the gradient at a point
P = {x: 1, y: 2, z: 0}
g1_P = g1.subs(P)
print("grad f at (1, 2, 0) =", g1_P.T)
print("|grad f| at (1, 2, 0) =", sp.sqrt(sum(c**2 for c in g1_P)))


# ---------- 2. Scalar field in 2 variables ----------
print("\n=== 2. Gradient of f(x, y) = x^3 + 3*x*y^2 - 4*y ===")
f2 = x**3 + 3 * x * y**2 - 4 * y
g2 = gradient(f2, (x, y))
print("f =", f2)
print("grad f =", g2.T)
print("grad f at (1, 1) =", g2.subs({x: 1, y: 1}).T)


# ---------- 3. Directional derivative ----------
print("\n=== 3. Directional derivative of f(x, y, z) = x*y + y*z + z*x ===")
f3 = x * y + y * z + z * x
g3 = gradient(f3, (x, y, z))
point = {x: 1, y: 1, z: 1}
a = sp.Matrix([1, 2, 2])                     # direction vector
u = a / a.norm()                             # unit vector along a
print("grad f =", g3.T)
print("grad f at (1, 1, 1) =", g3.subs(point).T)
print("Unit direction u =", u.T)
dd = g3.subs(point).dot(u)
print("Directional derivative D_u f at (1, 1, 1) =", dd)
print("Maximum rate of change = |grad f| =", g3.subs(point).norm())


# ---------- 4. Gradient of a function of r = sqrt(x^2 + y^2 + z^2) ----------
print("\n=== 4. Gradient of f = r^2 and f = log(r) ===")
r = sp.sqrt(x**2 + y**2 + z**2)
print("grad(r^2) =", sp.simplify(gradient(r**2, (x, y, z))).T)
print("grad(log r) =", sp.simplify(gradient(sp.log(r), (x, y, z))).T)
print("(= r_vector / r^2)")


# ---------- 5. Unit normal to a surface ----------
print("\n=== 5. Unit normal to surface x^2 + y^2 + z = 9 at (1, 2, 4) ===")
phi = x**2 + y**2 + z
g5 = gradient(phi, (x, y, z)).subs({x: 1, y: 2, z: 4})
n = g5 / g5.norm()
print("grad(phi) at (1, 2, 4) =", g5.T)
print("Unit normal =", sp.simplify(n).T)


# ---------- 6. Numerical gradient using NumPy ----------
print("\n=== 6. Numerical check using NumPy (central difference) ===")
def f_num(p):
    X, Y, Z = p
    return X**2 * Y + Y * Z**2 + np.sin(X * Z)

def num_grad(f, p, h=1e-5):
    p = np.array(p, dtype=float)
    g = np.zeros_like(p)
    for i in range(len(p)):
        step = np.zeros_like(p)
        step[i] = h
        g[i] = (f(p + step) - f(p - step)) / (2 * h)
    return g

print("Numerical grad f at (1, 2, 0) =", np.round(num_grad(f_num, [1, 2, 0]), 5))
print("Matches symbolic result?:",
      np.allclose(num_grad(f_num, [1, 2, 0]), np.array(g1_P.T.tolist()[0], dtype=float), atol=1e-4))