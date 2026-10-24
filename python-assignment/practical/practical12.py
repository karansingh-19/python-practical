
import sympy as sp
import numpy as np

# ---------- Symbols ----------
x, y, z = sp.symbols('x y z')

# ---------- Divergence of a vector field ----------
def divergence(F, variables):
    # div F = dF1/dx + dF2/dy + dF3/dz
    return sum(sp.diff(Fi, v) for Fi, v in zip(F, variables))


# ---------- 1. Vector field in 3 variables ----------
print("=== 1. Divergence of F = (x^2*y, y^2*z, z^2*x) ===")
F1 = [x**2 * y, y**2 * z, z**2 * x]
div1 = divergence(F1, (x, y, z))
print("F =", F1)
print("div F =", div1)
print("div F at (1, 2, 3) =", div1.subs({x: 1, y: 2, z: 3}))


# ---------- 2. Vector field in 2 variables ----------
print("\n=== 2. Divergence of F = (x^2 - y^2, 2*x*y) ===")
F2 = [x**2 - y**2, 2 * x * y]
div2 = divergence(F2, (x, y))
print("F =", F2)
print("div F =", sp.simplify(div2))
print("div F at (1, 1) =", div2.subs({x: 1, y: 1}))


# ---------- 3. Divergence of the position vector r ----------
print("\n=== 3. Divergence of position vector r = (x, y, z) ===")
r_vec = [x, y, z]
print("div r =", divergence(r_vec, (x, y, z)))


# ---------- 4. Divergence of r/|r|^3 (inverse-square field) ----------
print("\n=== 4. Divergence of F = r / |r|^3 ===")
r = sp.sqrt(x**2 + y**2 + z**2)
F4 = [x / r**3, y / r**3, z / r**3]
print("div F =", sp.simplify(divergence(F4, (x, y, z))))


# ---------- 5. Solenoidal / irrotational check ----------
print("\n=== 5. Is F = (y*z, z*x, x*y) solenoidal? ===")
F5 = [y * z, z * x, x * y]
div5 = divergence(F5, (x, y, z))
print("div F =", div5)
print("Solenoidal (div F = 0)?:", sp.simplify(div5) == 0)


# ---------- 6. Divergence of a scalar multiple: div(phi*A) ----------
print("\n=== 6. Verify div(phi*A) = phi*div(A) + grad(phi).A ===")
phi = x**2 + y**2 + z**2
A = [x, y, z]
lhs = divergence([phi * Ai for Ai in A], (x, y, z))
grad_phi = [sp.diff(phi, v) for v in (x, y, z)]
rhs = phi * divergence(A, (x, y, z)) + sum(g * Ai for g, Ai in zip(grad_phi, A))
print("div(phi*A) =", sp.expand(lhs))
print("phi*div(A) + grad(phi).A =", sp.expand(rhs))
print("Identity verified?:", sp.simplify(lhs - rhs) == 0)


# ---------- 7. Numerical check using NumPy (central difference) ----------
print("\n=== 7. Numerical check using NumPy ===")
def F_num(p):
    X, Y, Z = p
    return np.array([X**2 * Y, Y**2 * Z, Z**2 * X])

def num_div(F, p, h=1e-5):
    p = np.array(p, dtype=float)
    total = 0.0
    for i in range(len(p)):
        step = np.zeros_like(p)
        step[i] = h
        total += (F(p + step)[i] - F(p - step)[i]) / (2 * h)
    return total

print("Numerical div F at (1, 2, 3) =", round(num_div(F_num, [1, 2, 3]), 5))
print("Matches symbolic result?:", np.isclose(num_div(F_num, [1, 2, 3]), float(div1.subs({x: 1, y: 2, z: 3})), atol=1e-4))